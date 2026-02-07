import { Routes } from '@angular/router';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { SiteListComponent } from './pages/site-list/site-list.component';
import { SiteDetailComponent } from './pages/site-detail/site-detail.component';
import { AnalyzeComponent } from './pages/analyze/analyze.component';
import { StatisticsComponent } from './pages/statistics/statistics.component';
import { MapComponent } from './pages/map/map.component';

export const routes: Routes = [
  { path: '', component: DashboardComponent },   
  { path: 'sites', component: SiteListComponent },
  { path: 'sites/:id', component: SiteDetailComponent },
  { path: 'analyze', component: AnalyzeComponent },
  { path: 'statistics', component: StatisticsComponent },
  { path: 'map', component: MapComponent } 
];
