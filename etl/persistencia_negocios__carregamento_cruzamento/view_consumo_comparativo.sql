create view consumo_comparativo as
select c.mes as mes_ref,
	   c.uf as uf,
       c.consumidor as consumidor,
       c.consumo as consumo_atual,
       (CASE WHEN o1.consumo is null then 0.00 else o1.consumo END) as consumo_mes_anterior,
	   (case
			when o1.consumo is null and c.consumo is null then 0
            when o1.consumo is null and c.consumo is not null then c.consumo
            when c.consumo is null and o1.consumo is not null then (0 - o1.consumo)
            else (c.consumo - o1.consumo)
		END) as variacao_consumo_mes,
	   TRUNCATE((case
			when o1.consumo is null and c.consumo is null then 0
            when o1.consumo is null and c.consumo is not null then 100
            when c.consumo is null and o1.consumo is not null then -100
            when o1.consumo = 0 and c.consumo = 0 then 0
            when o1.consumo = 0 and c.consumo > 0 then 100
            else ((c.consumo - o1.consumo)/o1.consumo) * 100
		END), 2) as taxa_variacao_consumo_mes,
       (CASE WHEN o2.consumo is null then 0.00 else o2.consumo END) as consumo_ano_anterior,
       (CASE
			when o2.consumo is null and c.consumo is null then 0
            when o2.consumo is null and c.consumo is not null then c.consumo
            when c.consumo is null and o1.consumo is not null then (0 - o2.consumo)
            else (c.consumo - o2.consumo) 
		END) as variaca_consumo_ano,
        TRUNCATE((case
			when o2.consumo is null and c.consumo is null then 0
            when o2.consumo is null and c.consumo is not null then 100
            when c.consumo is null and o2.consumo is not null then -100
            when o2.consumo = 0 and c.consumo = 0 then 0
            when o2.consumo = 0 and c.consumo > 0 then 100
            else ((c.consumo - o2.consumo)/o2.consumo) * 100
		END), 2) as taxa_variacao_consumo_ano,
        
        c.consumo_cativo as consuno_cativo_atual,
        (CASE WHEN o1.consumo_cativo is null then 0.00 else o1.consumo_cativo END) as consumo_cativo_mes_anterior,
        (case
			when o1.consumo_cativo is null and c.consumo_cativo is null then 0
            when o1.consumo_cativo is null and c.consumo_cativo is not null then c.consumo_cativo
            when c.consumo_cativo is null and o1.consumo_cativo is not null then (0 - o1.consumo_cativo)
            else (c.consumo_cativo - o1.consumo_cativo)
		END) as variacao_consumo_cativo_mes,
        TRUNCATE((case
			when o1.consumo_cativo is null and c.consumo_cativo is null then 0
            when o1.consumo_cativo is null and c.consumo_cativo is not null then 100
            when c.consumo_cativo is null and o1.consumo_cativo is not null then -100
            when o1.consumo_cativo = 0 and c.consumo_cativo = 0 then 0
            when o1.consumo_cativo = 0 and c.consumo_cativo > 0 then 100
            else ((c.consumo_cativo - o1.consumo_cativo)/o1.consumo_cativo) * 100
		END), 2) as taxa_variacao_consumo_cativo_mes,
        (CASE WHEN o2.consumo_cativo is null then 0.00 else o2.consumo_cativo END) as consumo_cativo_ano_anterior,
        (CASE
			when o2.consumo_cativo is null and c.consumo_cativo is null then 0
            when o2.consumo_cativo is null and c.consumo_cativo is not null then c.consumo_cativo
            when c.consumo_cativo is null and o1.consumo_cativo is not null then (0 - o2.consumo_cativo)
            else (c.consumo_cativo - o2.consumo_cativo) 
		END) as variaca_consumo_cativo_ano,
        TRUNCATE((case
			when o2.consumo_cativo is null and c.consumo_cativo is null then 0
            when o2.consumo_cativo is null and c.consumo_cativo is not null then 100
            when c.consumo_cativo is null and o2.consumo_cativo is not null then -100
            when o2.consumo_cativo = 0 and c.consumo_cativo = 0 then 0
            when o2.consumo_cativo = 0 and c.consumo_cativo > 0 then 100
            else ((c.consumo_cativo - o2.consumo_cativo)/o2.consumo_cativo) * 100
		END), 2) as taxa_variacao_consumo_cativo_ano
from consumo c
	 left join consumo o1 on o1.mes = DATE_SUB(c.mes, INTERVAL 1 MONTH)
				and o1.uf = c.uf and o1.consumidor = c.consumidor
	 left join consumo o2 on o2.mes = DATE_SUB(c.mes, INTERVAL 1 YEAR)
				and o2.uf = c.uf and o2.consumidor = c.consumidor
order by mes_ref asc;