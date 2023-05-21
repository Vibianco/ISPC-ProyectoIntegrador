import { Component } from '@angular/core';
import { ServicioCarritoService } from 'src/app/Servicios/servicio-carrito.service';
@Component({
  selector: 'app-crearifa',
  templateUrl: './crearifa.component.html',
  styleUrls: ['./crearifa.component.css']
})

export class CrearifaComponent {


  constructor(private miServicio:ServicioCarritoService){}

}
