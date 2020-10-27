import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProfileComponent } from './profile/profile.component';
import {DashboardComponent} from './dashboard/dashboard.component';
import {HomepageComponent} from './homepage/homepage.component';
import {AboutusComponent} from './aboutus/aboutus.component';

const routes: Routes = [
  {path: 'profile', component: ProfileComponent },
  {path: 'dashboard', component: DashboardComponent },
  {path: 'homepage', component: HomepageComponent},
  {path: 'aboutus', component: AboutusComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
