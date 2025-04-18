CREATE TABLE IF NOT EXISTS "tab_dim_usuario" (
	"id_usuario" bigint NOT NULL,
	"nome" varchar(255) NOT NULL,
	"email" varchar(255) NOT NULL,
	"telefone" varchar(255) NOT NULL,
	"nivel_acesso_sistema" varchar(255) NOT NULL,
	"log_auditar" boolean NOT NULL,
	PRIMARY KEY ("id_usuario")
);

CREATE TABLE IF NOT EXISTS "tab_dim_data" (
	"id_data" timestamp without time zone NOT NULL,
	"ano" bigint NOT NULL,
	"mes" varchar(255) NOT NULL,
	"dia" varchar(255) NOT NULL,
	"hora" varchar(255) NOT NULL,
	"minutos" varchar(255) NOT NULL,
	"segundos" varchar(255) NOT NULL,
	"milissegundos" varchar(255) NOT NULL,
	PRIMARY KEY ("id_data")
);

CREATE TABLE IF NOT EXISTS "tab_dim_localidade" (
	"id_localidade" bigint NOT NULL,
	"cep" varchar(255) NOT NULL,
	"logradouro" varchar(255) NOT NULL,
	"numero" varchar(255) NOT NULL,
	"complemento" varchar(255) NOT NULL,
	"bairro" varchar(255) NOT NULL,
	"cidade" varchar(255) NOT NULL,
	"estado" varchar(255) NOT NULL,
	"pais" varchar(255) NOT NULL,
	PRIMARY KEY ("id_localidade")
);

CREATE TABLE IF NOT EXISTS "tab_dim_fator_risco" (
	"id_fator_risco" bigint NOT NULL,
	"idade" bigint NOT NULL,
	"imc" double precision NOT NULL,
	"carga_tabagica" bigint NOT NULL,
	"hipertensao" bigint NOT NULL,
	"diabetes" bigint NOT NULL,
	PRIMARY KEY ("id_fator_risco")
);

CREATE TABLE IF NOT EXISTS "tab_dim_paciente" (
	"id_paciente" bigint NOT NULL,
	"prontuario_num" bigint NOT NULL,
	"contrato_num" bigint NOT NULL,
	"nome" varchar(255) NOT NULL,
	"cpf" varchar(255) NOT NULL,
	"cns_numero_sus" varchar(255) NOT NULL,
	"localidade" varchar(255) NOT NULL,
	PRIMARY KEY ("id_paciente")
);

CREATE TABLE IF NOT EXISTS "tab_dim_profissional" (
	"id_profissional" bigint NOT NULL,
	"nome" varchar(255) NOT NULL,
	"categoria" varchar(255) NOT NULL,
	"conselho_classe_num" bigint NOT NULL,
	"conselho_classe_estado" varchar(255) NOT NULL,
	"habilitado_exercicio" boolean NOT NULL,
	"cns_numero_cadastro" varchar(255) NOT NULL,
	"nivel_acesso_sistema" varchar(255) NOT NULL,
	"new_field_1" bigint NOT NULL,
	PRIMARY KEY ("id_profissional")
);

CREATE TABLE IF NOT EXISTS "tab_fato_evento_biometria" (
	"id_evento_biometria" serial NOT NULL UNIQUE,
	"id_paciente" bigint NOT NULL,
	"id_usuarios" bigint NOT NULL,
	"id_profissional" bigint NOT NULL,
	"id_data_evento" timestamp without time zone NOT NULL,
	"id_localidade" bigint NOT NULL,
	"id_fator_risco" bigint NOT NULL,
	"pas" bigint NOT NULL,
	"pad" bigint NOT NULL,
	"pam_lambda01" bigint NOT NULL,
	"freq_cardiaca" bigint,
	"data_input_sistema" timestamp without time zone NOT NULL,
	PRIMARY KEY ("id_evento_biometria")
);







ALTER TABLE "tab_fato_evento_biometria" ADD CONSTRAINT "tab_fato_evento_biometria_fk1" FOREIGN KEY ("id_paciente") REFERENCES "tab_dim_paciente"("id_paciente");

ALTER TABLE "tab_fato_evento_biometria" ADD CONSTRAINT "tab_fato_evento_biometria_fk2" FOREIGN KEY ("id_usuarios") REFERENCES "tab_dim_usuario"("id_usuario");

ALTER TABLE "tab_fato_evento_biometria" ADD CONSTRAINT "tab_fato_evento_biometria_fk3" FOREIGN KEY ("id_profissional") REFERENCES "tab_dim_profissional"("id_profissional");

ALTER TABLE "tab_fato_evento_biometria" ADD CONSTRAINT "tab_fato_evento_biometria_fk4" FOREIGN KEY ("id_data_evento") REFERENCES "tab_dim_data"("id_data");

ALTER TABLE "tab_fato_evento_biometria" ADD CONSTRAINT "tab_fato_evento_biometria_fk5" FOREIGN KEY ("id_localidade") REFERENCES "tab_dim_localidade"("id_localidade");

ALTER TABLE "tab_fato_evento_biometria" ADD CONSTRAINT "tab_fato_evento_biometria_fk6" FOREIGN KEY ("id_fator_risco") REFERENCES "tab_dim_fator_risco"("id_fator_risco");