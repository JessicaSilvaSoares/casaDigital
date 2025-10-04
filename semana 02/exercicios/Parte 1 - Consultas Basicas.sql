-- 1. Liste todos os clientes cadastrados
SELECT
	CLIENTEID,
	NOME,
	EMAIL,
	TELEFONE
FROM
	CLIENTES;

-- 2. Liste todos os produtos da categoria "Acessórios"
SELECT
	PRODUTOID,
	NOME,
	PRECO
FROM
	PRODUTOS
WHERE
	CATEGORIA = 'Acessórios';

-- 3. Mostre todos os pedidos feitos por Ana Silva
SELECT
	P.PEDIDOID,
	TO_CHAR(P.DATAPEDIDO, 'DD/MM/YYYY') AS DATA,
	C.NOME
FROM
	PEDIDOS P
	JOIN CLIENTES C
		ON P.CLIENTEID = C.CLIENTEID
WHERE
	C.CLIENTEID = 1;
