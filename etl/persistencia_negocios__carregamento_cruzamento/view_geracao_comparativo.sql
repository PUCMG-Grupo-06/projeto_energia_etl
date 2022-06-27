create view geracao_comparativo as
select g.mes as mes_ref,
	   g.uf as uf,
       g.fonte_energia as fonte_energia,
       g.total_energia_entregue as entregue_ref,
       (CASE
	        when o1.total_energia_entregue is null then 0.00
            else o1.total_energia_entregue
	    END) as entregue_mes_anterior,
	   (CASE
	        when o2.total_energia_entregue is null then 0.00
            else o2.total_energia_entregue
	    END) as entregue_ano_anterior,
	   (CASE
	        when o1.total_energia_entregue is null and g.total_energia_entregue is null then 0.00
            when o1.total_energia_entregue is null and g.total_energia_entregue is not null then g.total_energia_entregue
            when g.total_energia_entregue is null and o1.total_energia_entregue is not null then (0 - o1.total_energia_entregue)
            else (g.total_energia_entregue - o1.total_energia_entregue)
	    END) as variacao_energia_entregue_mes,
	   (CASE
	        when o2.total_energia_entregue is null and g.total_energia_entregue is null then 0.00
            when o2.total_energia_entregue is null and g.total_energia_entregue is not null then g.total_energia_entregue
            when g.total_energia_entregue is null and o1.total_energia_entregue is not null then (0 - o2.total_energia_entregue)
            else (g.total_energia_entregue - o2.total_energia_entregue)
	    END) as variacao_energia_entregue_ano,
	   TRUNCATE((case
			when o1.total_energia_entregue is null and g.total_energia_entregue is null then 0
            when o1.total_energia_entregue is null and g.total_energia_entregue is not null then 100
            when o1.total_energia_entregue = 0 and g.total_energia_entregue = 0 then 0
            when o1.total_energia_entregue = 0 and g.total_energia_entregue > 0 then 100
            when g.total_energia_entregue is null and o1.total_energia_entregue is not null then -100
            else ((g.total_energia_entregue - o1.total_energia_entregue)/o1.total_energia_entregue) * 100
		END), 2) as taxa_variacao_energia_entregue_mes,
	   TRUNCATE((case
			when o2.total_energia_entregue is null and g.total_energia_entregue is null then 0
            when o2.total_energia_entregue is null and g.total_energia_entregue is not null then 100
            when g.total_energia_entregue is null and o2.total_energia_entregue is not null then -100
            when o2.total_energia_entregue = 0 and g.total_energia_entregue = 0 then 0
            when o2.total_energia_entregue = 0 and g.total_energia_entregue > 0 then 100
            else ((g.total_energia_entregue - o2.total_energia_entregue)/o2.total_energia_entregue) * 100
		END), 2) as taxa_variacao_energia_entregue_ano,

       g.total_energia_recebida as recebida_ref,
       (CASE
	        when o1.total_energia_recebida is null then 0.00
            else o1.total_energia_recebida
	    END) as recebida_mes_anterior,
	   (CASE
	        when o2.total_energia_recebida is null then 0.00
            else o2.total_energia_recebida
	    END) as recebida_ano_anterior,
	   (CASE
	        when o1.total_energia_recebida is null and g.total_energia_recebida is null then 0.00
            when o1.total_energia_recebida is null and g.total_energia_recebida is not null then g.total_energia_recebida
            when g.total_energia_recebida is null and o1.total_energia_recebida is not null then (0 - o1.total_energia_recebida)
            else (g.total_energia_recebida - o1.total_energia_recebida)
	    END) as variacao_energia_recebida_mes,
	   (CASE
	        when o2.total_energia_recebida is null and g.total_energia_recebida is null then 0.00
            when o2.total_energia_recebida is null and g.total_energia_recebida is not null then g.total_energia_recebida
            when g.total_energia_recebida is null and o1.total_energia_recebida is not null then (0 - o2.total_energia_recebida	)
            else (g.total_energia_recebida - o2.total_energia_recebida)
	    END) as variacao_energia_recebida_ano,
	   TRUNCATE((case
			when o1.total_energia_recebida is null and g.total_energia_recebida is null then 0
            when o1.total_energia_recebida is null and g.total_energia_recebida is not null then 100
            when o1.total_energia_recebida = 0 and g.total_energia_recebida = 0 then 0
            when o1.total_energia_recebida = 0 and g.total_energia_recebida > 0 then 100
            when g.total_energia_recebida is null and o1.total_energia_recebida is not null then -100
            else ((g.total_energia_recebida - o1.total_energia_recebida)/o1.total_energia_recebida) * 100
		END), 2) as taxa_variacao_energia_recebida_mes,
	   TRUNCATE((case
			when o2.total_energia_recebida is null and g.total_energia_recebida is null then 0
            when o2.total_energia_recebida is null and g.total_energia_recebida is not null then 100
            when g.total_energia_recebida is null and o2.total_energia_recebida is not null then -100
            when o2.total_energia_recebida = 0 and g.total_energia_recebida = 0 then 0
            when o2.total_energia_recebida = 0 and g.total_energia_recebida > 0 then 100
            else ((g.total_energia_recebida - o2.total_energia_recebida)/o2.total_energia_recebida) * 100
		END), 2) as taxa_variacao_energia_recebida_ano,

	   g.total_capacidade as capacidade_ref,
       (CASE
	        when o1.total_capacidade is null then 0.00
            else o1.total_capacidade
	    END) as capacidade_mes_anterior,
	   (CASE
	        when o2.total_capacidade is null then 0.00
            else o2.total_capacidade
	    END) as capacidade_ano_anterior,
	   (CASE
	        when o1.total_capacidade is null and g.total_capacidade is null then 0.00
            when o1.total_capacidade is null and g.total_capacidade is not null then g.total_capacidade
            when g.total_capacidade is null and o1.total_capacidade is not null then (0 - o1.total_capacidade)
            else (g.total_capacidade - o1.total_capacidade)
	    END) as variacao_capacidade_mes,
	   (CASE
	        when o2.total_capacidade is null and g.total_capacidade is null then 0.00
            when o2.total_capacidade is null and g.total_capacidade is not null then g.total_capacidade
            when g.total_capacidade is null and o1.total_capacidade is not null then (0 - o2.total_capacidade)
            else (g.total_capacidade - o2.total_energia_entregue)
	    END) as variacao_capacidade_ano,
	   TRUNCATE((case
			when o1.total_capacidade is null and g.total_capacidade is null then 0
            when o1.total_capacidade is null and g.total_capacidade is not null then 100
            when o1.total_capacidade = 0 and g.total_capacidade = 0 then 0
            when o1.total_capacidade = 0 and g.total_capacidade > 0 then 100
            when g.total_capacidade is null and o1.total_capacidade is not null then -100
            else ((g.total_capacidade - o1.total_capacidade)/o1.total_capacidade) * 100
		END), 2) as taxa_variacao_capacidade_mes,
	   TRUNCATE((case
			when o2.total_capacidade is null and g.total_capacidade is null then 0
            when o2.total_capacidade is null and g.total_capacidade is not null then 100
            when g.total_capacidade is null and o2.total_capacidade is not null then -100
            when o2.total_capacidade = 0 and g.total_capacidade = 0 then 0
            when o2.total_capacidade = 0 and g.total_capacidade > 0 then 100
            else ((g.total_capacidade - o2.total_capacidade)/o2.total_capacidade) * 100
		END), 2) as taxa_variacao_capacidade_ano,
       
       g.total_geracao_centro_gravidade as geracao_centro_gravidade_ref,
       (CASE
	        when o1.total_geracao_centro_gravidade is null then 0.00
            else o1.total_geracao_centro_gravidade
	     END) as geracao_centro_gravidade_mes_anterior,
        (CASE
			when o2.total_geracao_centro_gravidade is null then 0.00
            else o2.total_geracao_centro_gravidade
		 END) as geracao_centro_gravidade_ano_anterior,
		(CASE
	        when o1.total_geracao_centro_gravidade is null and g.total_geracao_centro_gravidade is null then 0.00
            when o1.total_geracao_centro_gravidade is null and g.total_geracao_centro_gravidade is not null then g.total_geracao_centro_gravidade
            when g.total_geracao_centro_gravidade is null and o1.total_geracao_centro_gravidade is not null then (0 - o1.total_geracao_centro_gravidade)
            else (g.total_geracao_centro_gravidade - o1.total_geracao_centro_gravidade)
	    END) as variacao_geracao_centro_gravidade_mes,
	   (CASE
	        when o2.total_geracao_centro_gravidade is null and g.total_geracao_centro_gravidade is null then 0.00
            when o2.total_geracao_centro_gravidade is null and g.total_geracao_centro_gravidade is not null then g.total_geracao_centro_gravidade
            when g.total_geracao_centro_gravidade is null and o1.total_geracao_centro_gravidade is not null then (0 - o2.total_geracao_centro_gravidade)
            else (g.total_geracao_centro_gravidade - o2.total_geracao_centro_gravidade)
	    END) as variacao_geracao_centro_gravidade_ano,
        TRUNCATE((case
			when o1.total_geracao_centro_gravidade is null and g.total_geracao_centro_gravidade is null then 0
            when o1.total_geracao_centro_gravidade is null and g.total_geracao_centro_gravidade is not null then 100
            when g.total_geracao_centro_gravidade is null and o1.total_geracao_centro_gravidade is not null then -100
            when o1.total_geracao_centro_gravidade = 0 and g.total_geracao_centro_gravidade = 0 then 0
            when o1.total_geracao_centro_gravidade = 0 and g.total_geracao_centro_gravidade > 0 then 100
            else ((g.total_geracao_centro_gravidade - o1.total_geracao_centro_gravidade)/o1.total_geracao_centro_gravidade) * 100
		END), 2) as taxa_variacao_geracao_centro_gravidade_mes,
        TRUNCATE((case
			when o2.total_geracao_centro_gravidade is null and g.total_geracao_centro_gravidade is null then 0
            when o2.total_geracao_centro_gravidade is null and g.total_geracao_centro_gravidade is not null then 100
            when g.total_geracao_centro_gravidade is null and o2.total_geracao_centro_gravidade is not null then -100
            when o2.total_geracao_centro_gravidade = 0 and g.total_geracao_centro_gravidade = 0 then 0
            when o2.total_geracao_centro_gravidade = 0 and g.total_geracao_centro_gravidade > 0 then 100
            else ((g.total_geracao_centro_gravidade - o2.total_geracao_centro_gravidade)/o2.total_geracao_centro_gravidade) * 100
		END), 2) as taxa_variacao_geracao_centro_gravidade_ano
from geracao g
	 left join geracao o1 on o1.mes = DATE_SUB(g.mes, INTERVAL 1 MONTH)
						  and o1.uf = g.uf and o1.fonte_energia = g.fonte_energia
	 left join geracao o2 on o2.mes = DATE_SUB(g.mes, INTERVAL 1 YEAR)
						  and o2.uf = g.uf and o2.fonte_energia = g.fonte_energia
group by mes_ref,uf, fonte_energia, entregue_ref
order by g.mes asc;