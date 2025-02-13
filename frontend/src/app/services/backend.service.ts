import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BackendService {
  private apiUrl = environment.backendApiUrl;

  constructor(private http: HttpClient) {}

  login(email: string, senha: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/login`, { email, senha });
  }

  register(usuario: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/register`, usuario);
  }

  getFavoritos(): Observable<any> {
    return this.http.get(`${this.apiUrl}/favoritos`);
  }

  addFavorito(noticiaId: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/favoritos`, { noticiaId });
  }
}
