import { Component, OnInit } from '@angular/core';
import { NewsService } from '../../services/news.service';
import { CommonModule } from '@angular/common';
import { NzGridModule } from 'ng-zorro-antd/grid';
import { NzCardModule } from 'ng-zorro-antd/card';
import { NzSpinModule } from 'ng-zorro-antd/spin';

@Component({
  selector: 'app-news-list',
  imports: [CommonModule, NzGridModule, NzCardModule, NzSpinModule],
  templateUrl: './news-list.component.html',
  styleUrls: ['./news-list.component.scss']
})
export class NewsListComponent implements OnInit {
  noticias: any[] = [];
  nextPageToken: string | null = null;
  loading = true;

  constructor(private newsService: NewsService) {}

  ngOnInit() {
    this.newsService.news$.subscribe((news) => {
      this.noticias = news;
    });

    this.loadNews();
  }

  loadNews(nextPageToken?: string) {
    this.loading = true;
    
    const category = this.newsService.categorySelectedSubject.value;
    const country = this.newsService.countrySelectedSubject.value;

    this.newsService.getNewsByFilters(category, country, nextPageToken).subscribe({
      next: (data) => {
        if (data && data.results) {
          this.noticias = data.results;
          this.nextPageToken = data.nextPage || null;
        } else {
          console.warn('Nenhuma notícia encontrada.');
        }
        this.loading = false;
      },
      error: (error) => {
        console.error('Erro ao carregar notícias', error);
        this.loading = false;
      }
    });
  }

  nextPage() {
    if (this.nextPageToken) {
      this.loadNews(this.nextPageToken);
    }
  }
}
