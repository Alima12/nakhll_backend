# Generated by Django 3.2.14 on 2022-08-02 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0011_auto_20220731_1428'),
    ]

    operations = [
        migrations.RunSQL('''
            -- FUNCTION: public.bank_total_minted_not_burned_coins()

            -- DROP FUNCTION IF EXISTS public.bank_total_minted_not_burned_coins();

            CREATE OR REPLACE FUNCTION public.bank_total_minted_not_burned_coins(
                )
                RETURNS bigint
                LANGUAGE 'sql'
                COST 100
                VOLATILE PARALLEL SAFE
            AS $BODY$
            select
                sum(
                    case when not is_mint then -1 * value
                    else value
                    end
                )
            from bank_coinmintburn
            $BODY$;

            ALTER FUNCTION public.bank_total_minted_not_burned_coins()
                OWNER TO nakhll;
        ''', reverse_sql='DROP FUNCTION IF EXISTS public.bank_total_minted_not_burned_coins();'),
        migrations.RunSQL('''
            -- FUNCTION: public.check_balance_before_burn()

            -- DROP FUNCTION IF EXISTS public.check_balance_before_burn();

            CREATE OR REPLACE FUNCTION public.check_balance_before_burn()
                RETURNS trigger
                LANGUAGE 'plpgsql'
                COST 100
                VOLATILE NOT LEAKPROOF
            AS $BODY$
                        declare
                            coins_count integer;
                        begin
                            if not new.is_mint then
                                        coins_count := (select * from bank_total_minted_not_burned_coins());
                                        if (coins_count - new.value) < 0 then
                                            raise exception 'can not burn non minted coin';
                                        end if;
                            end if;
                            return new;
                        end;

            $BODY$;

            ALTER FUNCTION public.check_balance_before_burn()
                OWNER TO nakhll;
        ''', reverse_sql='DROP FUNCTION IF EXISTS public.bank_total_minted_not_burned_coins();'),
        migrations.RunSQL('''
            -- Trigger: check_balance_before_burn_before_insert

            -- DROP TRIGGER IF EXISTS check_balance_before_burn_before_insert ON public.bank_coinmintburn;

            CREATE TRIGGER check_balance_before_burn_before_insert
                BEFORE INSERT
                ON public.bank_coinmintburn
                FOR EACH ROW
                EXECUTE FUNCTION public.check_balance_before_burn();
        ''', reverse_sql='DROP TRIGGER IF EXISTS check_balance_before_burn_before_insert ON public.bank_coinmintburn;')
    ]
