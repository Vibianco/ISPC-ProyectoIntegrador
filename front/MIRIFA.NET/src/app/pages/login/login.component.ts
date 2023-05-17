import { Component } from '@angular/core';
import { ServicioUsuarioService } from 'src/app/servicio-usuario.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  constructor(private Miservicio:ServicioUsuarioService){}

  add(Miservicio: string) {
    this.MiServicio.muestraMensaje.push(Miservicio);
  }
}
