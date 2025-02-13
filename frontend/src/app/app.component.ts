import { Component, OnInit } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { NzIconModule } from 'ng-zorro-antd/icon';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { NzMenuModule } from 'ng-zorro-antd/menu';
import { NewsService } from './services/news.service';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [RouterLink, RouterOutlet, NzIconModule, NzLayoutModule, NzMenuModule, NgClass],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  isCollapsed = false;
  selectedCategory = '';
  selectedCountry = '';

  constructor(private newsService: NewsService) {}

  onCategorySelect(category: string): void {
    this.newsService.setCategorySelected(category);
    this.selectedCategory = category;
    this.applyFilters();
  }

  onCountrySelect(country: string): void {
    this.newsService.setCountrySelected(country);
    this.selectedCountry = country;
    this.applyFilters();
  }

  // Aplica os filtros acumulados de categoria e país
  applyFilters(nextPageToken?: string): void {
    const category = this.newsService.categorySelectedSubject.value;
    const country = this.newsService.countrySelectedSubject.value;

    this.newsService.getNewsByFilters(category, country, nextPageToken).subscribe((data) => {
      console.log('Notícias filtradas por categoria e país', data);
      this.newsService.setNews(data.results);  // Atualiza as notícias
    });
  }

  onDeselectCategory(): void {
    this.newsService.setCategorySelected('');
    this.applyFilters();
  }

  onDeselectCountry(): void {
    this.newsService.setCountrySelected('');
    this.applyFilters();
  }
}
