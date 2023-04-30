import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BienvenidaComponent } from './pages/bienvenida/bienvenida.component';
import { CrearifaComponent } from './pages/crearifa/crearifa.component';
import { RifasactualesComponent } from './pages/rifasactuales/rifasactuales.component';
import { PlanesComponent } from './pages/planes/planes.component';
import { ContactoComponent } from './pages/contacto/contacto.component';
import { FaqComponent } from './pages/faq/faq.component';
import { LoginComponent } from './pages/login/login.component';
import { CarritoComponent } from './ecommerce/carrito/carrito.component';
import { TerminosComponent } from './pages/terminos/terminos.component';
import { RegistroComponent } from './pages/registro/registro.component';

const routes: Routes = [
  {path: '', component:BienvenidaComponent},
  {path: 'inicio', component:BienvenidaComponent},
  {path: 'crearifa', component:CrearifaComponent},
  {path: 'rifasactuales', component:RifasactualesComponent},
  {path: 'planes', component:PlanesComponent},
  {path: 'contacto', component:ContactoComponent},
  {path: 'faq', component:FaqComponent},
  {path: 'login', component:LoginComponent},
  {path: 'register', component:RegistroComponent},
  {path: 'carrito', component:CarritoComponent},
  {path: 'terminos', component:TerminosComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
