import { Component } from '@angular/core';
import { ServicioUsuarioService } from 'src/app/Servicios/servicio-usuario.service';
import { FormBuilder } from '@angular/forms';
import {Validators} from '@angular/forms'


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  export class LoginComponent {
    invalido = "";
    LoginForm = this.formBuilder.group({
      user:['',[Validators.required, Validators.minLength(5)]],
      password:['',[Validators.required,Validators.minLength(8)]],

    })


  get user(){
    return this.LoginForm.get("usuario")
  }
  get password(){
    return this.LoginForm.get("contraseña")
  }
 

  onEnviar(event: Event){
    event.preventDefault;
    if(this.LoginForm.valid){
      alert("Enviar al servidor...")
    }else{
      this.LoginForm.markAllAsTouched()
      this.invalido = "is-invalid border-danger"
    }
  }

  constructor(private Miservicio:ServicioUsuarioService, private formBuilder:FormBuilder){}
}
}
