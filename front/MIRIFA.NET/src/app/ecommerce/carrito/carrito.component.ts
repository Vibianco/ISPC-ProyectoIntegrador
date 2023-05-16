import { Component } from '@angular/core';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent {


  constructor(private miServicio:ServicioMirifaService){}

  add(miServicio: string) {
    this.miServicio.muestraMensaje.push(miServicio);
  }
}
