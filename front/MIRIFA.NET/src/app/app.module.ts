import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SharedModule } from './shared/shared.module';
import { EcommerceModule } from './ecommerce/ecommerce.module';
import { PagesModule } from './pages/pages.module';
import { ServicioMirifaService } from './servicio-mirifa.service';
import { ServicioCarritoService } from './servicio-carrito.service';
import { ServicioUsuarioService } from './servicio-usuario.service';



@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    CommonModule,
    BrowserModule,
    AppRoutingModule,
    SharedModule,
    EcommerceModule,
    PagesModule
  ],
  providers: [ServicioMirifaService,ServicioCarritoService,ServicioUsuarioService],
  bootstrap: [AppComponent]
})
export class AppModule { }
