import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  private apiUrl = environment.newsApiUrl;
  private apiKey = environment.newsApiKey;

  private newsSubject = new BehaviorSubject<any[]>([]);
  news$ = this.newsSubject.asObservable();

  categorySelectedSubject = new BehaviorSubject<string>('');
  categorySelected$ = this.categorySelectedSubject.asObservable();

  countrySelectedSubject = new BehaviorSubject<string>('');
  countrySelected$ = this.countrySelectedSubject.asObservable();

  constructor(private http: HttpClient) {}

  getLatestNews(nextPageToken?: string): Observable<any> {
    const url = nextPageToken 
      ? `${this.apiUrl}?apiKey=${this.apiKey}&page=${nextPageToken}&image=1&language=pt,en,es,fr,it` 
      : `${this.apiUrl}?apiKey=${this.apiKey}&image=1&language=pt,en,es,fr,it`;
    return this.http.get<any>(url);
  }

  getNewsByFilters(category: string, country: string, nextPageToken?: string): Observable<any> {
    let url = `${this.apiUrl}?apiKey=${this.apiKey}&image=1&language=pt,en,es,fr,it`;

    if (category) {
      url += `&category=${category}`;
    }

    if (country) {
      url += `&country=${country}`;
    }

    if (nextPageToken) {
      url += `&page=${nextPageToken}`;
    }

    return this.http.get<any>(url);
  }

  setNews(news: any[]) {
    this.newsSubject.next(news);  
  }

  setCategorySelected(category: string) {
    this.categorySelectedSubject.next(category);
  }

  setCountrySelected(country: string) {
    this.countrySelectedSubject.next(country);
  }
}
