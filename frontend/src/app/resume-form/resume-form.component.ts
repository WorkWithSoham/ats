import { CommonModule } from '@angular/common';
import { Component, ElementRef, ViewChild, NgModule } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';
import { DataService } from '../../services/api/data.service';
import { HttpResponse } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { ResumeAnalysis } from '../interfaces/ResumeAnalysis';
import { LoadingComponent } from '../loading/loading.component';

const ALLOWED_FILE_TYPE = '.pdf';

@Component({
  selector: 'app-resume-form',
  standalone: true,
  imports: [RouterOutlet, CommonModule, FormsModule, LoadingComponent],
  templateUrl: './resume-form.component.html',
  styleUrl: './resume-form.component.css',
})
export class ResumeFormComponent {
  constructor(private dataService: DataService) {}
  @ViewChild('fileInput', { static: false }) fileInput!: ElementRef;

  allowedFileType = ALLOWED_FILE_TYPE;

  router = new Router();
  isUploading = false;
  fileUrl!: string | null;
  uploadFile!: File | null;
  backendFileName!: string | null;
  job_description: string = '';
  resumeAnalysis: ResumeAnalysis = {};

  handleChange(event: any) {
    const data = new FormData();

    const file = event.target.files[0];
    this.uploadFile = file;

    data.append('pdf_file', this.uploadFile!, this.uploadFile?.name);

    this.dataService
      .submit_resume(data)
      .subscribe((res: HttpResponse<Blob>) => {
        var downloadURL = window.URL.createObjectURL(res.body!);
        this.fileUrl = downloadURL;
        this.backendFileName = res.headers.get('content-disposition');
      });
  }

  handleRemovesFile() {
    if (this.fileInput && this.fileInput.nativeElement) {
      this.fileInput.nativeElement.value = null;
    }

    this.uploadFile = null;
    this.fileUrl = null;

    this.dataService.remove_file(this.backendFileName!).subscribe((res) => {});
  }

  handleUploadFile() {
    localStorage.setItem('fileUrl', this.fileUrl!);
    this.isUploading = true;

    this.dataService
      .get_resume_review(this.backendFileName!, this.job_description)
      .subscribe((res) => {
        var jsonString: string = res.msg;
        jsonString = jsonString.replace(/```/g, '').replace(/json/g, '').trim();
        this.resumeAnalysis = JSON.parse(jsonString.replace(/\n/g, ''));
        console.log(this.resumeAnalysis);
        this.router.navigateByUrl('/analysis', {
          state: [JSON.stringify(this.resumeAnalysis)],
        });
      });
  }
}
