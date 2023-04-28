import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrearifaComponent } from './crearifa.component';

describe('CrearifaComponent', () => {
  let component: CrearifaComponent;
  let fixture: ComponentFixture<CrearifaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CrearifaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CrearifaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
