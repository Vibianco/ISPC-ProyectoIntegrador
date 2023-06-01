import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ServicioCarritoService {

  constructor() { }

  muestraMensaje (mensaje:string){

    alert(mensaje);
  }
}
