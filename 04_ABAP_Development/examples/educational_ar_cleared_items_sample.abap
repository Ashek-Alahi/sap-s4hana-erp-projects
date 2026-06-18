" Educational sample reconstructed from documented project design, not exported from a production SAP system.
" Purpose: show the shape of an A/R cleared items report using customer master and cleared item tables.

REPORT zedu_ar_cleared_items_sample.

TABLES: bsad, kna1.

PARAMETERS p_bukrs TYPE bsad-bukrs OBLIGATORY.
SELECT-OPTIONS: s_kunnr FOR bsad-kunnr,
                s_budat FOR bsad-budat,
                s_augdt FOR bsad-augdt.

TYPES: BEGIN OF ty_output,
         bukrs TYPE bsad-bukrs,
         kunnr TYPE bsad-kunnr,
         name1 TYPE kna1-name1,
         belnr TYPE bsad-belnr,
         gjahr TYPE bsad-gjahr,
         budat TYPE bsad-budat,
         augbl TYPE bsad-augbl,
         augdt TYPE bsad-augdt,
         shkzg TYPE bsad-shkzg,
         dmbtr TYPE bsad-dmbtr,
       END OF ty_output.

DATA gt_output TYPE STANDARD TABLE OF ty_output.

SELECT a~bukrs, a~kunnr, b~name1, a~belnr, a~gjahr,
       a~budat, a~augbl, a~augdt, a~shkzg, a~dmbtr
  FROM bsad AS a
  INNER JOIN kna1 AS b ON b~kunnr = a~kunnr
  INTO TABLE @gt_output
  WHERE a~bukrs = @p_bukrs
    AND a~kunnr IN @s_kunnr
    AND a~budat IN @s_budat
    AND a~augdt IN @s_augdt.

cl_demo_output=>display( gt_output ).
