import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ServicioMirifaService {

  constructor() { }

  muestraMensaje (mensaje:string){

    alert(mensaje);
  }
}
