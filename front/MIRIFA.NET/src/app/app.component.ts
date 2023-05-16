import { Component } from '@angular/core';
import { ServicioMirifaService } from './servicio-mirifa.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'MIRIFA.NET';

  constructor(private miServicio:ServicioMirifaService){}

  this.miServicio.muestraMensaje("Tu registro ha sido exitoso")
}


