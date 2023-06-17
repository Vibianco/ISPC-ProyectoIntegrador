import { Component, OnInit } from '@angular/core';
import { ServicioCarritoService } from 'src/app/Servicios/servicio-carrito.service';
import { Router } from '@angular/router';
import { AuthtokenService } from 'src/app/Servicios/auth/authtoken.service';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent implements OnInit{
  carritoActual:any;

  constructor(private carrito:ServicioCarritoService, private Auth: AuthtokenService, private router : Router){
    this.ObtenerDatos();
  }

  ObtenerDatos(){
    this.carrito.ObtenerCarrito().subscribe({
      next:(carritoActualData)=>{
        this.carritoActual=carritoActualData;
      },
      error: (errorData) =>{
        console.error(errorData)
      }
    })
  }
  
  OnClickEliminar(indice:number){
    this.carrito.EliminarCarrito(indice).subscribe();
    alert("Rifa eliminada con exito");
    this.ObtenerDatos();
  }
  OnClickAdd(){
    this.carrito.AñadirCarrito().subscribe();
    this.ObtenerDatos();
  }

  Opcion(opcion:number){
    return opcion
  }

  OnClick(){
    this.router.navigate(['/compra'])
  }

  ngOnInit(): void {
    
  }

}
