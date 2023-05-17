import { Component } from '@angular/core';
import { ServicioCarritoService } from 'src/app/servicio-carrito.service';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent {


  constructor(private miServicio:ServicioCarritoService){}

  add(miServis: string) {
    this.miServis.muestraMensaje.push(miServis);
  }
}
