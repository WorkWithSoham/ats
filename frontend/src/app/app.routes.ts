import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ResumeFormComponent } from './resume-form/resume-form.component';
import { ResumeAnalysisComponent } from './resume-analysis/resume-analysis.component';

export const routes: Routes = [
  { path: '', component: HomeComponent, title: 'Home Page' },
  { path: 'upload', component: ResumeFormComponent, title: 'Resume Form' },
  {
    path: 'analysis',
    component: ResumeAnalysisComponent,
    title: 'Resume Analysis',
  },
  { path: '**', redirectTo: '' }
];
