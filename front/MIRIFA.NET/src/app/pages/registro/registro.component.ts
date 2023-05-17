import { Component } from '@angular/core';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent {


  constructor(private Miservicio:ServicioUsuarioService){}

  add(Miservicio: string) {
    this.MiServicio.muestraMensaje.push(Miservicio);
  }
}
