import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { RegisterFormComponent } from './register-form/register-form.component';


const routes: Routes = [
  { path: 'register-form', component: RegisterFormComponent },
  { path: 'login', component: LoginComponent },
  { path: '**', redirectTo: '/register-form', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
