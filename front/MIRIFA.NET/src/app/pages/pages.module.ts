import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { BienvenidaComponent } from './bienvenida/bienvenida.component';
import { CrearifaComponent } from './crearifa/crearifa.component';
import { RifasactualesComponent } from './rifasactuales/rifasactuales.component';
import { PlanesComponent } from './planes/planes.component';
import { ContactoComponent } from './contacto/contacto.component';
import { FaqComponent } from './faq/faq.component';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { TerminosComponent } from './terminos/terminos.component';
import { AppRoutingModule } from '../app-routing.module';
import { ReactiveFormsModule } from '@angular/forms';



@NgModule({
  declarations: [
    BienvenidaComponent,
    CrearifaComponent,
    RifasactualesComponent,
    PlanesComponent,
    ContactoComponent,
    FaqComponent,
    LoginComponent,
    RegistroComponent,
    TerminosComponent,
  ],
  imports: [
    CommonModule,
    AppRoutingModule,
    ReactiveFormsModule
  ],
  exports: [
    BienvenidaComponent,
    CrearifaComponent,
    RifasactualesComponent,
    PlanesComponent,
    ContactoComponent,
    FaqComponent,
    LoginComponent,
    RegistroComponent,
    TerminosComponent
  ]
})
export class PagesModule { }
