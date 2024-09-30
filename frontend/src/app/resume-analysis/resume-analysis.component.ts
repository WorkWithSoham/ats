import { Component, OnInit } from '@angular/core';
import { ResumeAnalysis } from '../interfaces/ResumeAnalysis';
import { DataService } from '../../services/api/data.service';
import { NavigationStart, Router } from '@angular/router';

@Component({
  selector: 'app-resume-analysis',
  standalone: true,
  imports: [],
  templateUrl: './resume-analysis.component.html',
  styleUrl: './resume-analysis.component.css',
})
export class ResumeAnalysisComponent implements OnInit {
  constructor(private router: Router) {}

  ngOnInit(): void {
    this.router.events.subscribe((event) => {
      this.fileUrl = localStorage.getItem('fileUrl')!;
    });
  }

  resumeAnalysis: ResumeAnalysis = JSON.parse(window.history.state[0]);
  fileUrl: string = localStorage.getItem('fileUrl')!;
}
