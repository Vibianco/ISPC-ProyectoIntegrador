import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CarritoComponent } from './carrito/carrito.component';
import { CompraComponent } from './compra/compra.component';
import { ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    CarritoComponent,
    CompraComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule
  ],
  exports: [
    CarritoComponent,
    CompraComponent
  ]
})
export class EcommerceModule { }
