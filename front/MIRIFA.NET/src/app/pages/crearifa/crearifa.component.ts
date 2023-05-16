import { Component } from '@angular/core';

@Component({
  selector: 'app-crearifa',
  templateUrl: './crearifa.component.html',
  styleUrls: ['./crearifa.component.css']
})
export class CrearifaComponent {


  constructor(private miServicio:ServicioMirifaService){}

  add(miServicio: string) {
    this.miServicio.muestraMensaje.push(miServicio);
  }
}
