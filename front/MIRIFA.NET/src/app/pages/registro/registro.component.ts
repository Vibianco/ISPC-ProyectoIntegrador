import { Component } from '@angular/core';
import { ServicioUsuarioService } from 'src/app/Servicios/servicio-usuario.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import {Validators} from '@angular/forms'

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent {

forma!: FormGroup;

constructor(private Miservicio:ServicioUsuarioService, private formBuilder:FormBuilder){
  this.crearRegistro();

}

get nombreNoValido(){

  return this.forma.get("nombre")?.invalid && this.forma.get("nombre")?.touched;

}

get apellidoNoValido(){

  return this.forma.get("apellido")?.invalid && this.forma.get("apellido")?.touched;
  
}

get dniNoValido(){

  return this.forma.get("dni")?.invalid && this.forma.get("dni")?.touched;
  
}

get paisNoValido(){

  return this.forma.get("pais")?.invalid && this.forma.get("pais")?.touched;
  
}

get ciudadNoValido(){

  return this.forma.get("ciudad")?.invalid && this.forma.get("ciudad")?.touched;
  
}

get telefonoNoValido(){

  return this.forma.get("telefono")?.invalid && this.forma.get("telefono")?.touched;
  
}

get usuarioNoValido(){

  return this.forma.get("nombreusuario")?.invalid && this.forma.get("nombreusuario")?.touched;
  
}

get emailNoValido(){

  return this.forma.get("email")?.invalid && this.forma.get("email")?.touched;
  
}

get passwordNoValido(){

  return this.forma.get("password")?.invalid && this.forma.get("password")?.touched;
  
}

get password1NoValido(){

  return this.forma.get("password1")?.invalid && this.forma.get("password1")?.touched;
  
}



crearRegistro (){
  this.forma = this.formBuilder.group ({

    nombre:['',[Validators.required, Validators.minLength(2),Validators.maxLength(30)]],
    apellido:['',[Validators.required,Validators.minLength(2),Validators.maxLength(30)]],
    dni:['',[Validators.required,Validators.pattern(/^([0-9])*$/)]],
    pais:['',Validators.required],
    ciudad:['',Validators.required],
    telefono:['',[Validators.required,Validators.minLength(7),Validators.maxLength(10),Validators.pattern(/^([0-9])*$/)]],
    nombreusuario:['',[Validators.required,Validators.min(5)]],
    email:['',[Validators.required,Validators.pattern(/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/)]],
    password:['',[Validators.required,Validators.minLength(8)]],
    password1:['',Validators.required]

  },{

    Validators: this.passwordIguales('password','password1')

  }
  )
}

registrarse(){
  console.log(this.forma);

  this.passNoValido();


  if (this.forma.invalid) {

    return Object.values (this.forma.controls).forEach(control=>{

      control.markAllAsTouched();

    })

  }
}

passNoValido () {

  const pass = this.forma.get('password')?.value;
  const pass1 = this.forma.get('password1')?.value;

  if (pass !== pass1) {
    return true;
  } else {
    return false;
  }

}

passwordIguales (passName:string, pass1Name:string){

  return (fromGrup: FormGroup) => {

    const passControl = fromGrup.get(passName);
    const pass1Control = fromGrup.get(pass1Name);

    if (passControl?.value === pass1Control?.value) {
      pass1Control?.setErrors(null);
    } else {
      pass1Control?.setErrors({noEsIgual:true})
  }

}
}

}
