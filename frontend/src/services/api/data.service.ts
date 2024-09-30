import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  constructor(private http: HttpClient) {}

  localhost: string = 'http://127.0.0.1:8000/';

  submit_resume = (data: {}) => {
    return this.http.post(this.localhost + 'api/resume-form/', data, {
      observe: 'response',
      responseType: 'blob',
    });
  };

  get_resume_review = (
    file_name: string,
    job_description: string
  ): Observable<any> => {
    return this.http.post(this.localhost + 'api/get-review/', {
      file_name: file_name,
      job_description: job_description,
    });
  };

  remove_file = (file_name: string) => {
    return this.http.post(this.localhost + 'api/remove-file/', {
      file_name: file_name,
    });
  };
}
