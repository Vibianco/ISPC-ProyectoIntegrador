import { Component } from '@angular/core';
import { ServicioCarritoService } from 'src/app/Servicios/servicio-carrito.service';
import { FormBuilder } from '@angular/forms';
import {Validators} from '@angular/forms'

@Component({
  selector: 'app-crearifa',
  templateUrl: './crearifa.component.html',
  styleUrls: ['./crearifa.component.css']
})

export class CrearifaComponent {
  invalido = "";
  crearRifaForm = this.formBuilder.group({
    titulo:['',[Validators.required, Validators.minLength(5)]],
    descripcion:['',[Validators.required,Validators.minLength(20)]],
    organizador:['',[Validators.required,Validators.minLength(5)]],
    premio1:['',[Validators.required,Validators.minLength(5)]],
    premio2:['',[Validators.required,Validators.minLength(5)]],
    premio3:['',[Validators.required,Validators.minLength(5)]],
    numRifas:['',[Validators.required,Validators.min(100)]],
    monto:['',[Validators.required,Validators.min(100)]],
    titular:['',[Validators.required,Validators.minLength(5)]],
    cbu:['',[Validators.required,Validators.minLength(22)]],
    banco:['',[Validators.required,Validators.minLength(5)]],
    fecha:['',[Validators.required]],
  })
  constructor(private miServicio:ServicioCarritoService, private formBuilder:FormBuilder){

  }
  get Titulo(){
    return this.crearRifaForm.get("titulo")
  }
  get Descripcion(){
    return this.crearRifaForm.get("descripcion")
  }
  get Organizador(){
    return this.crearRifaForm.get("organizador")
  }
  get Premio1(){
    return this.crearRifaForm.get("premio1")
  }
  get Premio2(){
    return this.crearRifaForm.get("premio2")
  }
  get Premio3(){
    return this.crearRifaForm.get("premio3")
  }
  get NumRifas(){
    return this.crearRifaForm.get("numRifas")
  }
  get Monto(){
    return this.crearRifaForm.get("monto")
  }
  get Titular(){
    return this.crearRifaForm.get("titular")
  }
  get Cbu(){
    return this.crearRifaForm.get("cbu")
  }
  get Banco(){
    return this.crearRifaForm.get("banco")
  }
  get Fecha(){
    return this.crearRifaForm.get("fecha")
  }
  get RifasDestacadas(){
    return this.crearRifaForm.get("rifasDestacadas")
  }

  onEnviar(event: Event){
    event.preventDefault;
    if(this.crearRifaForm.valid){
      alert("Enviar al servidor...")
    }else{
      this.crearRifaForm.markAllAsTouched()
      this.invalido = "is-invalid border-danger"
    }
  }
}
