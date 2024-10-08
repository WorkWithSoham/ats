import {
  AfterViewInit,
  Component,
  ElementRef,
  HostListener,
  OnInit,
  ViewChild,
  ViewChildren,
} from '@angular/core';
import { ResumeAnalysis } from '../interfaces/ResumeAnalysis';
import { DataService } from '../../services/api/data.service';
import { NavigationStart, Router } from '@angular/router';
import { res } from '../temp-data/data';
import { NgClass, NgFor, NgIf } from '@angular/common';
import { SvgComponent } from '../svg/svg.component';

@Component({
  selector: 'app-resume-analysis',
  standalone: true,
  imports: [NgFor, NgIf, NgClass, SvgComponent],
  templateUrl: './resume-analysis.component.html',
  styleUrl: './resume-analysis.component.css',
})
export class ResumeAnalysisComponent {
  constructor(private router: Router) {}
  @ViewChild('circle', { static: true }) circle!: ElementRef;

  ngAfterViewInit(): void {
    const progress = this.circle.nativeElement;
    let degree = 0;
    const targetDegree = parseInt(progress.getAttribute('data-degree')!);
    const color = this.getColor(this.resumeAnalysis.percentage_match!);
    const number = progress.querySelector('.number');

    const interval = setInterval(() => {
      degree += 1;
      if (degree > targetDegree) {
        clearInterval(interval);
        return;
      }
      progress.style.background = `conic-gradient(${color} ${degree}%, #222 0%)`;
    }, 15);
  }

  // ngOnInit(): void {
  //   this.router.events.subscribe(() => {
  //     this.fileUrl = localStorage.getItem('fileUrl')!;
  //   });
  // }

  // resumeAnalysis: ResumeAnalysis = JSON.parse(window.history.state[0]);
  // fileUrl: string = localStorage.getItem('fileUrl')!;

  value: number = 65;
  resumeAnalysis: ResumeAnalysis = res;
  fileUrl: string =
    'https://www.resumebuilder.com/wp-content/uploads/2023/12/Homepage-2.png';

  getColor(percentage: number): string {
    if (percentage >= 80) {
      return '#00cc99'; // Green for high matches
    } else if (percentage >= 60) {
      return '#ff9d1c'; // Yellow for moderate matches
    } else if (percentage >= 40) {
      return '#ef4d02'; // Orange for lower matches
    } else {
      return '#d63636'; // Red for very low matches
    }
  }
}
