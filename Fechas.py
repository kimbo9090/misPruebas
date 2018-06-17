class Fecha:
    def __init__(self,dia,mes,anio):

        self.dia = dia
        self.mes = mes
        self.anio = anio
        if not isinstance(dia,int) or not isinstance(mes,int) or not isinstance(anio,int):
            raise ValueError('Tienes que introducir un numero')

        if self.dia <=0 or self.dia >=32:
            raise ValueError('No puede haber un dia menor que 0 o mayor que 31')
        if self.mes >12 or self.mes <=0:
            raise ValueError('No puede haber meses mayor que 31 o un mes menor que 0')
        if self.anio > 2999 or self.anio < 1923:
            raise ValueError('Limite de fechas alcanzado')
        if self.mes == 2 and self.dia >29:
            raise ValueError('No puedes hacer una fecha mayor que 29 en febrero')
        if self.mes == 4 and self.dia>30 \
                or self.mes == 6 and self.dia>30 or\
                self.mes == 9 and self.dia>30\
                or self.mes == 11 and self.dia >30:
            raise ValueError('Fecha invalida')

    def esBisiesto(self):
        if self.anio % 4 == 0:
            return True
        else:
            return False

    def diaSiguiente(self):
        if self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or \
        self.mes == 8 or self.mes == 10 or self.mes == 12:
            if self.dia ==31:
                if self.mes == 12:
                    if self.anio == 2999:
                        print('No se puede sumar el dia, ya que esta en el año limite')
                    else:
                        print(1,1,self.anio+1)
                else:
                    print(1,self.mes+1,self.anio)
            else:
                print(self.dia+1,self.mes,self.anio)


        elif self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11:
            if self.dia == 30:
                print(1,self.mes+1,self.anio)
            else:
                print(self.dia+1,self.mes,self.anio)

        elif self.mes == 2:
            if self.esBisiesto():
                if self.dia ==29:
                    print(1,self.mes+1,self.anio)
                else:
                    print(self.dia+1,self.mes,self.anio)

            elif not self.esBisiesto():
                if self.dia == 28:
                    print(1,self.mes+1,self.anio)
                else:
                    print(self.dia+1,self.mes,self.anio)


f = Fecha(31,12,1996)

print(f.diaSiguiente())

