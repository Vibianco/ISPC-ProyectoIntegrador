import { Component } from '@angular/core';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent {


  constructor(private miServicio:ServicioMirifaService){}

  add(miServicio: string) {
    this.miServicio.muestraMensaje.push(miServicio);
  }
}
