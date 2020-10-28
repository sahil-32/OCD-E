import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  log_email:string;
  log_password:string;
  reg_email:string;
  reg_password:string;
  reg_confirm_password:string;

  login(){

  }

  register(){

  }

  constructor() { }

  ngOnInit(): void {
  }

}
