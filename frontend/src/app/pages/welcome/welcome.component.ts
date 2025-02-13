import { Component } from '@angular/core';
import { NewsListComponent } from "../../components/news-list/news-list.component";

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrl: './welcome.component.scss',
  imports: [NewsListComponent]
})
export class WelcomeComponent {
  constructor() {}
}
