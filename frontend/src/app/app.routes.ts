import { Routes } from '@angular/router';
import { PerfilComponent } from './pages/perfil/perfil.component';
import { FavoritesComponent } from './pages/favorites/favorites.component';

export const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: '/welcome' },
  { path: 'welcome', loadChildren: () => import('./pages/welcome/welcome.routes').then(m => m.WELCOME_ROUTES) },
  { path: 'perfil', component: PerfilComponent },
  { path: 'favorites', component: FavoritesComponent },
];
