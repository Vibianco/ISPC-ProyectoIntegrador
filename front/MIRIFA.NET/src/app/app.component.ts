import { Component } from '@angular/core';
import { ServicioMirifaService } from './servicio-mirifa.service';
import { ServicioCarritoService } from './servicio-carrito.service';
import { ServicioUsuarioService } from './servicio-usuario.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'MIRIFA.NET';

  constructor(private miServicio:ServicioMirifaService){}

  this.miServicio.muestraMensaje("Tu registro ha sido exitoso")

  constructor (private miServis:ServicioCarritoService)
  this.miServis.muestraMensaje("Tu compra ha sido exitosa")

  constructor(private Miservicio:ServicioUsuarioService)
  this.Miservicio.muestraMensaje("Tu registro ha sido exitoso")
}


