# Portfolio
El programa se compone de la clase Portfolio y Stock. Esta última clase crea al momento de instanciarse un historico de valores para todo el año 2024, considerando 30 días para cada mes, con el fín de modelar el método que devuelve el precio de la acción en cada unos de los días del año. La clase Portfolio es la encargada de instanciar Stocks mediante el input `stocks_diversification`, que además indica el peso a diversificar en cada acción disponible. También recibe como input `investment` como la inversión total del portafolio y `purchase_portfolio_date` como la fecha en la que se adquiere el portafolio.

## Flujo
El método profit de Portfolio es el encargado de imprimir todas información solicitada, para obtener el profit se sigue el flujo de almacenar las cantidades de acciones que se adquirieron con la inversión inicial. Luego, se obtiene el valor del portafolio en función de la cantidad de acciones que posee y actualizar el valor del portafolio en función del valor de cada acción. Finalmente se resta el valor incial del portafolio con el valor actual según la fecha final entregada. Por últiom, para aplicar la formula de rentabilidad anual se tomo el supuesto de que un 1 año contiene 365 días.

## Ejecutar programa
```bash
python portfolio.py
