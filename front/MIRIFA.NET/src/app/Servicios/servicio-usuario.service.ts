import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ServicioUsuarioService {

  constructor() { }

  muestraMensaje (mensaje:string){

    alert(mensaje);
  }
}