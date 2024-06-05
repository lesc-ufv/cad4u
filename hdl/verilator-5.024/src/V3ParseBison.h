/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_CONTENT_CAD4U_HDL_VERILATOR_5_024_SRC_V3PARSEBISON_PRETMP_H_INCLUDED
# define YY_YY_CONTENT_CAD4U_HDL_VERILATOR_5_024_SRC_V3PARSEBISON_PRETMP_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    yaFLOATNUM = 258,              /* "FLOATING-POINT NUMBER"  */
    yaID__ETC = 259,               /* "IDENTIFIER"  */
    yaID__CC = 260,                /* "IDENTIFIER-::"  */
    yaID__LEX = 261,               /* "IDENTIFIER-in-lex"  */
    yaID__aTYPE = 262,             /* "TYPE-IDENTIFIER"  */
    yaINTNUM = 263,                /* "INTEGER NUMBER"  */
    yaTIMENUM = 264,               /* "TIME NUMBER"  */
    yaSTRING = 265,                /* "STRING"  */
    yaSTRING__IGNORE = 266,        /* "STRING-ignored"  */
    yaTIMINGSPEC = 267,            /* "TIMING SPEC ELEMENT"  */
    ygenSTRENGTH = 268,            /* "STRENGTH keyword (strong1/etc)"  */
    yaTABLELINE = 269,             /* "TABLE LINE"  */
    yaSCHDR = 270,                 /* "`systemc_header BLOCK"  */
    yaSCINT = 271,                 /* "`systemc_ctor BLOCK"  */
    yaSCIMP = 272,                 /* "`systemc_dtor BLOCK"  */
    yaSCIMPH = 273,                /* "`systemc_interface BLOCK"  */
    yaSCCTOR = 274,                /* "`systemc_implementation BLOCK"  */
    yaSCDTOR = 275,                /* "`systemc_imp_header BLOCK"  */
    yVLT_CLOCKER = 276,            /* "clocker"  */
    yVLT_CLOCK_ENABLE = 277,       /* "clock_enable"  */
    yVLT_COVERAGE_BLOCK_OFF = 278, /* "coverage_block_off"  */
    yVLT_COVERAGE_OFF = 279,       /* "coverage_off"  */
    yVLT_COVERAGE_ON = 280,        /* "coverage_on"  */
    yVLT_FORCEABLE = 281,          /* "forceable"  */
    yVLT_FULL_CASE = 282,          /* "full_case"  */
    yVLT_HIER_BLOCK = 283,         /* "hier_block"  */
    yVLT_INLINE = 284,             /* "inline"  */
    yVLT_ISOLATE_ASSIGNMENTS = 285, /* "isolate_assignments"  */
    yVLT_LINT_OFF = 286,           /* "lint_off"  */
    yVLT_LINT_ON = 287,            /* "lint_on"  */
    yVLT_NO_CLOCKER = 288,         /* "no_clocker"  */
    yVLT_NO_INLINE = 289,          /* "no_inline"  */
    yVLT_PARALLEL_CASE = 290,      /* "parallel_case"  */
    yVLT_PROFILE_DATA = 291,       /* "profile_data"  */
    yVLT_PUBLIC = 292,             /* "public"  */
    yVLT_PUBLIC_FLAT = 293,        /* "public_flat"  */
    yVLT_PUBLIC_FLAT_RD = 294,     /* "public_flat_rd"  */
    yVLT_PUBLIC_FLAT_RW = 295,     /* "public_flat_rw"  */
    yVLT_PUBLIC_MODULE = 296,      /* "public_module"  */
    yVLT_SC_BV = 297,              /* "sc_bv"  */
    yVLT_SFORMAT = 298,            /* "sformat"  */
    yVLT_SPLIT_VAR = 299,          /* "split_var"  */
    yVLT_TIMING_OFF = 300,         /* "timing_off"  */
    yVLT_TIMING_ON = 301,          /* "timing_on"  */
    yVLT_TRACING_OFF = 302,        /* "tracing_off"  */
    yVLT_TRACING_ON = 303,         /* "tracing_on"  */
    yVLT_D_BLOCK = 304,            /* "--block"  */
    yVLT_D_COST = 305,             /* "--cost"  */
    yVLT_D_FILE = 306,             /* "--file"  */
    yVLT_D_FUNCTION = 307,         /* "--function"  */
    yVLT_D_LEVELS = 308,           /* "--levels"  */
    yVLT_D_LINES = 309,            /* "--lines"  */
    yVLT_D_MATCH = 310,            /* "--match"  */
    yVLT_D_MODEL = 311,            /* "--model"  */
    yVLT_D_MODULE = 312,           /* "--module"  */
    yVLT_D_MTASK = 313,            /* "--mtask"  */
    yVLT_D_RULE = 314,             /* "--rule"  */
    yVLT_D_SCOPE = 315,            /* "--scope"  */
    yVLT_D_TASK = 316,             /* "--task"  */
    yVLT_D_VAR = 317,              /* "--var"  */
    yaD_PLI = 318,                 /* "${pli-system}"  */
    yaT_NOUNCONNECTED = 319,       /* "`nounconnecteddrive"  */
    yaT_RESETALL = 320,            /* "`resetall"  */
    yaT_UNCONNECTED_PULL0 = 321,   /* "`unconnected_drive pull0"  */
    yaT_UNCONNECTED_PULL1 = 322,   /* "`unconnected_drive pull1"  */
    ya1STEP = 323,                 /* "1step"  */
    yACCEPT_ON = 324,              /* "accept_on"  */
    yALIAS = 325,                  /* "alias"  */
    yALWAYS = 326,                 /* "always"  */
    yALWAYS_COMB = 327,            /* "always_comb"  */
    yALWAYS_FF = 328,              /* "always_ff"  */
    yALWAYS_LATCH = 329,           /* "always_latch"  */
    yAND = 330,                    /* "and"  */
    yASSERT = 331,                 /* "assert"  */
    yASSIGN = 332,                 /* "assign"  */
    yASSUME = 333,                 /* "assume"  */
    yAUTOMATIC = 334,              /* "automatic"  */
    yBEFORE = 335,                 /* "before"  */
    yBEGIN = 336,                  /* "begin"  */
    yBIND = 337,                   /* "bind"  */
    yBINS = 338,                   /* "bins"  */
    yBINSOF = 339,                 /* "binsof"  */
    yBIT = 340,                    /* "bit"  */
    yBREAK = 341,                  /* "break"  */
    yBUF = 342,                    /* "buf"  */
    yBUFIF0 = 343,                 /* "bufif0"  */
    yBUFIF1 = 344,                 /* "bufif1"  */
    yBYTE = 345,                   /* "byte"  */
    yCASE = 346,                   /* "case"  */
    yCASEX = 347,                  /* "casex"  */
    yCASEZ = 348,                  /* "casez"  */
    yCHANDLE = 349,                /* "chandle"  */
    yCHECKER = 350,                /* "checker"  */
    yCLASS = 351,                  /* "class"  */
    yCLOCKING = 352,               /* "clocking"  */
    yCMOS = 353,                   /* "cmos"  */
    yCONSTRAINT = 354,             /* "constraint"  */
    yCONST__ETC = 355,             /* "const"  */
    yCONST__LEX = 356,             /* "const-in-lex"  */
    yCONST__REF = 357,             /* "const-then-ref"  */
    yCONTEXT = 358,                /* "context"  */
    yCONTINUE = 359,               /* "continue"  */
    yCOVER = 360,                  /* "cover"  */
    yCOVERGROUP = 361,             /* "covergroup"  */
    yCOVERPOINT = 362,             /* "coverpoint"  */
    yCROSS = 363,                  /* "cross"  */
    yDEASSIGN = 364,               /* "deassign"  */
    yDEFAULT = 365,                /* "default"  */
    yDEFPARAM = 366,               /* "defparam"  */
    yDISABLE = 367,                /* "disable"  */
    yDIST = 368,                   /* "dist"  */
    yDO = 369,                     /* "do"  */
    yEDGE = 370,                   /* "edge"  */
    yELSE = 371,                   /* "else"  */
    yEND = 372,                    /* "end"  */
    yENDCASE = 373,                /* "endcase"  */
    yENDCHECKER = 374,             /* "endchecker"  */
    yENDCLASS = 375,               /* "endclass"  */
    yENDCLOCKING = 376,            /* "endclocking"  */
    yENDFUNCTION = 377,            /* "endfunction"  */
    yENDGENERATE = 378,            /* "endgenerate"  */
    yENDGROUP = 379,               /* "endgroup"  */
    yENDINTERFACE = 380,           /* "endinterface"  */
    yENDMODULE = 381,              /* "endmodule"  */
    yENDPACKAGE = 382,             /* "endpackage"  */
    yENDPRIMITIVE = 383,           /* "endprimitive"  */
    yENDPROGRAM = 384,             /* "endprogram"  */
    yENDPROPERTY = 385,            /* "endproperty"  */
    yENDSEQUENCE = 386,            /* "endsequence"  */
    yENDSPECIFY = 387,             /* "endspecify"  */
    yENDTABLE = 388,               /* "endtable"  */
    yENDTASK = 389,                /* "endtask"  */
    yENUM = 390,                   /* "enum"  */
    yEVENT = 391,                  /* "event"  */
    yEVENTUALLY = 392,             /* "eventually"  */
    yEXPECT = 393,                 /* "expect"  */
    yEXPORT = 394,                 /* "export"  */
    yEXTENDS = 395,                /* "extends"  */
    yEXTERN = 396,                 /* "extern"  */
    yFINAL = 397,                  /* "final"  */
    yFIRST_MATCH = 398,            /* "first_match"  */
    yFOR = 399,                    /* "for"  */
    yFORCE = 400,                  /* "force"  */
    yFOREACH = 401,                /* "foreach"  */
    yFOREVER = 402,                /* "forever"  */
    yFORK = 403,                   /* "fork"  */
    yFORKJOIN = 404,               /* "forkjoin"  */
    yFUNCTION = 405,               /* "function"  */
    yGENERATE = 406,               /* "generate"  */
    yGENVAR = 407,                 /* "genvar"  */
    yGLOBAL__CLOCKING = 408,       /* "global-then-clocking"  */
    yGLOBAL__ETC = 409,            /* "global"  */
    yGLOBAL__LEX = 410,            /* "global-in-lex"  */
    yHIGHZ0 = 411,                 /* "highz0"  */
    yHIGHZ1 = 412,                 /* "highz1"  */
    yIF = 413,                     /* "if"  */
    yIFF = 414,                    /* "iff"  */
    yIGNORE_BINS = 415,            /* "ignore_bins"  */
    yILLEGAL_BINS = 416,           /* "illegal_bins"  */
    yIMPLEMENTS = 417,             /* "implements"  */
    yIMPLIES = 418,                /* "implies"  */
    yIMPORT = 419,                 /* "import"  */
    yINITIAL = 420,                /* "initial"  */
    yINOUT = 421,                  /* "inout"  */
    yINPUT = 422,                  /* "input"  */
    yINSIDE = 423,                 /* "inside"  */
    yINT = 424,                    /* "int"  */
    yINTEGER = 425,                /* "integer"  */
    yINTERCONNECT = 426,           /* "interconnect"  */
    yINTERFACE = 427,              /* "interface"  */
    yINTERSECT = 428,              /* "intersect"  */
    yJOIN = 429,                   /* "join"  */
    yJOIN_ANY = 430,               /* "join_any"  */
    yJOIN_NONE = 431,              /* "join_none"  */
    yLET = 432,                    /* "let"  */
    yLOCALPARAM = 433,             /* "localparam"  */
    yLOCAL__COLONCOLON = 434,      /* "local-then-::"  */
    yLOCAL__ETC = 435,             /* "local"  */
    yLOCAL__LEX = 436,             /* "local-in-lex"  */
    yLOGIC = 437,                  /* "logic"  */
    yLONGINT = 438,                /* "longint"  */
    yMATCHES = 439,                /* "matches"  */
    yMODPORT = 440,                /* "modport"  */
    yMODULE = 441,                 /* "module"  */
    yNAND = 442,                   /* "nand"  */
    yNEGEDGE = 443,                /* "negedge"  */
    yNETTYPE = 444,                /* "nettype"  */
    yNEW__ETC = 445,               /* "new"  */
    yNEW__LEX = 446,               /* "new-in-lex"  */
    yNEW__PAREN = 447,             /* "new-then-paren"  */
    yNEXTTIME = 448,               /* "nexttime"  */
    yNMOS = 449,                   /* "nmos"  */
    yNOR = 450,                    /* "nor"  */
    yNOT = 451,                    /* "not"  */
    yNOTIF0 = 452,                 /* "notif0"  */
    yNOTIF1 = 453,                 /* "notif1"  */
    yNULL = 454,                   /* "null"  */
    yOR = 455,                     /* "or"  */
    yOUTPUT = 456,                 /* "output"  */
    yPACKAGE = 457,                /* "package"  */
    yPACKED = 458,                 /* "packed"  */
    yPARAMETER = 459,              /* "parameter"  */
    yPMOS = 460,                   /* "pmos"  */
    yPOSEDGE = 461,                /* "posedge"  */
    yPRIMITIVE = 462,              /* "primitive"  */
    yPRIORITY = 463,               /* "priority"  */
    yPROGRAM = 464,                /* "program"  */
    yPROPERTY = 465,               /* "property"  */
    yPROTECTED = 466,              /* "protected"  */
    yPULL0 = 467,                  /* "pull0"  */
    yPULL1 = 468,                  /* "pull1"  */
    yPULLDOWN = 469,               /* "pulldown"  */
    yPULLUP = 470,                 /* "pullup"  */
    yPURE = 471,                   /* "pure"  */
    yRAND = 472,                   /* "rand"  */
    yRANDC = 473,                  /* "randc"  */
    yRANDCASE = 474,               /* "randcase"  */
    yRANDOMIZE = 475,              /* "randomize"  */
    yRANDSEQUENCE = 476,           /* "randsequence"  */
    yRCMOS = 477,                  /* "rcmos"  */
    yREAL = 478,                   /* "real"  */
    yREALTIME = 479,               /* "realtime"  */
    yREF = 480,                    /* "ref"  */
    yREG = 481,                    /* "reg"  */
    yREJECT_ON = 482,              /* "reject_on"  */
    yRELEASE = 483,                /* "release"  */
    yREPEAT = 484,                 /* "repeat"  */
    yRESTRICT = 485,               /* "restrict"  */
    yRETURN = 486,                 /* "return"  */
    yRNMOS = 487,                  /* "rnmos"  */
    yRPMOS = 488,                  /* "rpmos"  */
    yRTRAN = 489,                  /* "rtran"  */
    yRTRANIF0 = 490,               /* "rtranif0"  */
    yRTRANIF1 = 491,               /* "rtranif1"  */
    ySCALARED = 492,               /* "scalared"  */
    ySEQUENCE = 493,               /* "sequence"  */
    ySHORTINT = 494,               /* "shortint"  */
    ySHORTREAL = 495,              /* "shortreal"  */
    ySIGNED = 496,                 /* "signed"  */
    ySOFT = 497,                   /* "soft"  */
    ySOLVE = 498,                  /* "solve"  */
    ySPECIFY = 499,                /* "specify"  */
    ySPECPARAM = 500,              /* "specparam"  */
    ySTATIC__CONSTRAINT = 501,     /* "static-then-constraint"  */
    ySTATIC__ETC = 502,            /* "static"  */
    ySTATIC__LEX = 503,            /* "static-in-lex"  */
    ySTRING = 504,                 /* "string"  */
    ySTRONG = 505,                 /* "strong"  */
    ySTRONG0 = 506,                /* "strong0"  */
    ySTRONG1 = 507,                /* "strong1"  */
    ySTRUCT = 508,                 /* "struct"  */
    ySUPER = 509,                  /* "super"  */
    ySUPPLY0 = 510,                /* "supply0"  */
    ySUPPLY1 = 511,                /* "supply1"  */
    ySYNC_ACCEPT_ON = 512,         /* "sync_accept_on"  */
    ySYNC_REJECT_ON = 513,         /* "sync_reject_on"  */
    yS_ALWAYS = 514,               /* "s_always"  */
    yS_EVENTUALLY = 515,           /* "s_eventually"  */
    yS_NEXTTIME = 516,             /* "s_nexttime"  */
    yS_UNTIL = 517,                /* "s_until"  */
    yS_UNTIL_WITH = 518,           /* "s_until_with"  */
    yTABLE = 519,                  /* "table"  */
    yTASK = 520,                   /* "task"  */
    yTHIS = 521,                   /* "this"  */
    yTHROUGHOUT = 522,             /* "throughout"  */
    yTIME = 523,                   /* "time"  */
    yTIMEPRECISION = 524,          /* "timeprecision"  */
    yTIMEUNIT = 525,               /* "timeunit"  */
    yTRAN = 526,                   /* "tran"  */
    yTRANIF0 = 527,                /* "tranif0"  */
    yTRANIF1 = 528,                /* "tranif1"  */
    yTRI = 529,                    /* "tri"  */
    yTRI0 = 530,                   /* "tri0"  */
    yTRI1 = 531,                   /* "tri1"  */
    yTRIAND = 532,                 /* "triand"  */
    yTRIOR = 533,                  /* "trior"  */
    yTRIREG = 534,                 /* "trireg"  */
    yTRUE = 535,                   /* "true"  */
    yTYPEDEF = 536,                /* "typedef"  */
    yTYPE__EQ = 537,               /* "type-then-eqneq"  */
    yTYPE__ETC = 538,              /* "type"  */
    yTYPE__LEX = 539,              /* "type-in-lex"  */
    yUNION = 540,                  /* "union"  */
    yUNIQUE = 541,                 /* "unique"  */
    yUNIQUE0 = 542,                /* "unique0"  */
    yUNSIGNED = 543,               /* "unsigned"  */
    yUNTIL = 544,                  /* "until"  */
    yUNTIL_WITH = 545,             /* "until_with"  */
    yUNTYPED = 546,                /* "untyped"  */
    yVAR = 547,                    /* "var"  */
    yVECTORED = 548,               /* "vectored"  */
    yVIRTUAL__CLASS = 549,         /* "virtual-then-class"  */
    yVIRTUAL__ETC = 550,           /* "virtual"  */
    yVIRTUAL__INTERFACE = 551,     /* "virtual-then-interface"  */
    yVIRTUAL__LEX = 552,           /* "virtual-in-lex"  */
    yVIRTUAL__anyID = 553,         /* "virtual-then-identifier"  */
    yVOID = 554,                   /* "void"  */
    yWAIT = 555,                   /* "wait"  */
    yWAIT_ORDER = 556,             /* "wait_order"  */
    yWAND = 557,                   /* "wand"  */
    yWEAK = 558,                   /* "weak"  */
    yWEAK0 = 559,                  /* "weak0"  */
    yWEAK1 = 560,                  /* "weak1"  */
    yWHILE = 561,                  /* "while"  */
    yWILDCARD = 562,               /* "wildcard"  */
    yWIRE = 563,                   /* "wire"  */
    yWITHIN = 564,                 /* "within"  */
    yWITH__BRA = 565,              /* "with-then-["  */
    yWITH__CUR = 566,              /* "with-then-{"  */
    yWITH__ETC = 567,              /* "with"  */
    yWITH__LEX = 568,              /* "with-in-lex"  */
    yWITH__PAREN = 569,            /* "with-then-("  */
    yWOR = 570,                    /* "wor"  */
    yWREAL = 571,                  /* "wreal"  */
    yXNOR = 572,                   /* "xnor"  */
    yXOR = 573,                    /* "xor"  */
    yD_ACOS = 574,                 /* "$acos"  */
    yD_ACOSH = 575,                /* "$acosh"  */
    yD_ASIN = 576,                 /* "$asin"  */
    yD_ASINH = 577,                /* "$asinh"  */
    yD_ATAN = 578,                 /* "$atan"  */
    yD_ATAN2 = 579,                /* "$atan2"  */
    yD_ATANH = 580,                /* "$atanh"  */
    yD_BITS = 581,                 /* "$bits"  */
    yD_BITSTOREAL = 582,           /* "$bitstoreal"  */
    yD_BITSTOSHORTREAL = 583,      /* "$bitstoshortreal"  */
    yD_C = 584,                    /* "$c"  */
    yD_CAST = 585,                 /* "$cast"  */
    yD_CEIL = 586,                 /* "$ceil"  */
    yD_CHANGED = 587,              /* "$changed"  */
    yD_CHANGED_GCLK = 588,         /* "$changed_gclk"  */
    yD_CLOG2 = 589,                /* "$clog2"  */
    yD_COS = 590,                  /* "$cos"  */
    yD_COSH = 591,                 /* "$cosh"  */
    yD_COUNTBITS = 592,            /* "$countbits"  */
    yD_COUNTONES = 593,            /* "$countones"  */
    yD_DIMENSIONS = 594,           /* "$dimensions"  */
    yD_DISPLAY = 595,              /* "$display"  */
    yD_DISPLAYB = 596,             /* "$displayb"  */
    yD_DISPLAYH = 597,             /* "$displayh"  */
    yD_DISPLAYO = 598,             /* "$displayo"  */
    yD_DIST_CHI_SQUARE = 599,      /* "$dist_chi_square"  */
    yD_DIST_ERLANG = 600,          /* "$dist_erlang"  */
    yD_DIST_EXPONENTIAL = 601,     /* "$dist_exponential"  */
    yD_DIST_NORMAL = 602,          /* "$dist_normal"  */
    yD_DIST_POISSON = 603,         /* "$dist_poisson"  */
    yD_DIST_T = 604,               /* "$dist_t"  */
    yD_DIST_UNIFORM = 605,         /* "$dist_uniform"  */
    yD_DUMPALL = 606,              /* "$dumpall"  */
    yD_DUMPFILE = 607,             /* "$dumpfile"  */
    yD_DUMPFLUSH = 608,            /* "$dumpflush"  */
    yD_DUMPLIMIT = 609,            /* "$dumplimit"  */
    yD_DUMPOFF = 610,              /* "$dumpoff"  */
    yD_DUMPON = 611,               /* "$dumpon"  */
    yD_DUMPPORTS = 612,            /* "$dumpports"  */
    yD_DUMPVARS = 613,             /* "$dumpvars"  */
    yD_ERROR = 614,                /* "$error"  */
    yD_EXIT = 615,                 /* "$exit"  */
    yD_EXP = 616,                  /* "$exp"  */
    yD_FATAL = 617,                /* "$fatal"  */
    yD_FCLOSE = 618,               /* "$fclose"  */
    yD_FDISPLAY = 619,             /* "$fdisplay"  */
    yD_FDISPLAYB = 620,            /* "$fdisplayb"  */
    yD_FDISPLAYH = 621,            /* "$fdisplayh"  */
    yD_FDISPLAYO = 622,            /* "$fdisplayo"  */
    yD_FELL = 623,                 /* "$fell"  */
    yD_FELL_GCLK = 624,            /* "$fell_gclk"  */
    yD_FEOF = 625,                 /* "$feof"  */
    yD_FERROR = 626,               /* "$ferror"  */
    yD_FFLUSH = 627,               /* "$fflush"  */
    yD_FGETC = 628,                /* "$fgetc"  */
    yD_FGETS = 629,                /* "$fgets"  */
    yD_FINISH = 630,               /* "$finish"  */
    yD_FLOOR = 631,                /* "$floor"  */
    yD_FMONITOR = 632,             /* "$fmonitor"  */
    yD_FMONITORB = 633,            /* "$fmonitorb"  */
    yD_FMONITORH = 634,            /* "$fmonitorh"  */
    yD_FMONITORO = 635,            /* "$fmonitoro"  */
    yD_FOPEN = 636,                /* "$fopen"  */
    yD_FREAD = 637,                /* "$fread"  */
    yD_FREWIND = 638,              /* "$frewind"  */
    yD_FSCANF = 639,               /* "$fscanf"  */
    yD_FSEEK = 640,                /* "$fseek"  */
    yD_FSTROBE = 641,              /* "$fstrobe"  */
    yD_FSTROBEB = 642,             /* "$fstrobeb"  */
    yD_FSTROBEH = 643,             /* "$fstrobeh"  */
    yD_FSTROBEO = 644,             /* "$fstrobeo"  */
    yD_FTELL = 645,                /* "$ftell"  */
    yD_FWRITE = 646,               /* "$fwrite"  */
    yD_FWRITEB = 647,              /* "$fwriteb"  */
    yD_FWRITEH = 648,              /* "$fwriteh"  */
    yD_FWRITEO = 649,              /* "$fwriteo"  */
    yD_GLOBAL_CLOCK = 650,         /* "$global_clock"  */
    yD_HIGH = 651,                 /* "$high"  */
    yD_HYPOT = 652,                /* "$hypot"  */
    yD_INCREMENT = 653,            /* "$increment"  */
    yD_INFO = 654,                 /* "$info"  */
    yD_ISUNBOUNDED = 655,          /* "$isunbounded"  */
    yD_ISUNKNOWN = 656,            /* "$isunknown"  */
    yD_ITOR = 657,                 /* "$itor"  */
    yD_LEFT = 658,                 /* "$left"  */
    yD_LN = 659,                   /* "$ln"  */
    yD_LOG10 = 660,                /* "$log10"  */
    yD_LOW = 661,                  /* "$low"  */
    yD_MONITOR = 662,              /* "$monitor"  */
    yD_MONITORB = 663,             /* "$monitorb"  */
    yD_MONITORH = 664,             /* "$monitorh"  */
    yD_MONITORO = 665,             /* "$monitoro"  */
    yD_MONITOROFF = 666,           /* "$monitoroff"  */
    yD_MONITORON = 667,            /* "$monitoron"  */
    yD_ONEHOT = 668,               /* "$onehot"  */
    yD_ONEHOT0 = 669,              /* "$onehot0"  */
    yD_PAST = 670,                 /* "$past"  */
    yD_POW = 671,                  /* "$pow"  */
    yD_PRINTTIMESCALE = 672,       /* "$printtimescale"  */
    yD_RANDOM = 673,               /* "$random"  */
    yD_READMEMB = 674,             /* "$readmemb"  */
    yD_READMEMH = 675,             /* "$readmemh"  */
    yD_REALTIME = 676,             /* "$realtime"  */
    yD_REALTOBITS = 677,           /* "$realtobits"  */
    yD_REWIND = 678,               /* "$rewind"  */
    yD_RIGHT = 679,                /* "$right"  */
    yD_ROOT = 680,                 /* "$root"  */
    yD_ROSE = 681,                 /* "$rose"  */
    yD_ROSE_GCLK = 682,            /* "$rose_gclk"  */
    yD_RTOI = 683,                 /* "$rtoi"  */
    yD_SAMPLED = 684,              /* "$sampled"  */
    yD_SFORMAT = 685,              /* "$sformat"  */
    yD_SFORMATF = 686,             /* "$sformatf"  */
    yD_SHORTREALTOBITS = 687,      /* "$shortrealtobits"  */
    yD_SIGNED = 688,               /* "$signed"  */
    yD_SIN = 689,                  /* "$sin"  */
    yD_SINH = 690,                 /* "$sinh"  */
    yD_SIZE = 691,                 /* "$size"  */
    yD_SQRT = 692,                 /* "$sqrt"  */
    yD_SSCANF = 693,               /* "$sscanf"  */
    yD_STABLE = 694,               /* "$stable"  */
    yD_STABLE_GCLK = 695,          /* "$stable_gclk"  */
    yD_STACKTRACE = 696,           /* "$stacktrace"  */
    yD_STIME = 697,                /* "$stime"  */
    yD_STOP = 698,                 /* "$stop"  */
    yD_STROBE = 699,               /* "$strobe"  */
    yD_STROBEB = 700,              /* "$strobeb"  */
    yD_STROBEH = 701,              /* "$strobeh"  */
    yD_STROBEO = 702,              /* "$strobeo"  */
    yD_SWRITE = 703,               /* "$swrite"  */
    yD_SWRITEB = 704,              /* "$swriteb"  */
    yD_SWRITEH = 705,              /* "$swriteh"  */
    yD_SWRITEO = 706,              /* "$swriteo"  */
    yD_SYSTEM = 707,               /* "$system"  */
    yD_TAN = 708,                  /* "$tan"  */
    yD_TANH = 709,                 /* "$tanh"  */
    yD_TESTPLUSARGS = 710,         /* "$test$plusargs"  */
    yD_TIME = 711,                 /* "$time"  */
    yD_TIMEFORMAT = 712,           /* "$timeformat"  */
    yD_TIMEPRECISION = 713,        /* "$timeprecision"  */
    yD_TIMEUNIT = 714,             /* "$timeunit"  */
    yD_TYPENAME = 715,             /* "$typename"  */
    yD_UNGETC = 716,               /* "$ungetc"  */
    yD_UNIT = 717,                 /* "$unit"  */
    yD_UNPACKED_DIMENSIONS = 718,  /* "$unpacked_dimensions"  */
    yD_UNSIGNED = 719,             /* "$unsigned"  */
    yD_URANDOM = 720,              /* "$urandom"  */
    yD_URANDOM_RANGE = 721,        /* "$urandom_range"  */
    yD_VALUEPLUSARGS = 722,        /* "$value$plusargs"  */
    yD_WARNING = 723,              /* "$warning"  */
    yD_WRITE = 724,                /* "$write"  */
    yD_WRITEB = 725,               /* "$writeb"  */
    yD_WRITEH = 726,               /* "$writeh"  */
    yD_WRITEMEMB = 727,            /* "$writememb"  */
    yD_WRITEMEMH = 728,            /* "$writememh"  */
    yD_WRITEO = 729,               /* "$writeo"  */
    yVL_CLOCKER = 730,             /* "/\*verilator clocker*\/"  */
    yVL_CLOCK_ENABLE = 731,        /* "/\*verilator clock_enable*\/"  */
    yVL_COVERAGE_BLOCK_OFF = 732,  /* "/\*verilator coverage_block_off*\/"  */
    yVL_FORCEABLE = 733,           /* "/\*verilator forceable*\/"  */
    yVL_FULL_CASE = 734,           /* "/\*verilator full_case*\/"  */
    yVL_HIER_BLOCK = 735,          /* "/\*verilator hier_block*\/"  */
    yVL_INLINE_MODULE = 736,       /* "/\*verilator inline_module*\/"  */
    yVL_ISOLATE_ASSIGNMENTS = 737, /* "/\*verilator isolate_assignments*\/"  */
    yVL_NO_CLOCKER = 738,          /* "/\*verilator no_clocker*\/"  */
    yVL_NO_INLINE_MODULE = 739,    /* "/\*verilator no_inline_module*\/"  */
    yVL_NO_INLINE_TASK = 740,      /* "/\*verilator no_inline_task*\/"  */
    yVL_PARALLEL_CASE = 741,       /* "/\*verilator parallel_case*\/"  */
    yVL_PUBLIC = 742,              /* "/\*verilator public*\/"  */
    yVL_PUBLIC_FLAT = 743,         /* "/\*verilator public_flat*\/"  */
    yVL_PUBLIC_FLAT_ON = 744,      /* "/\*verilator public_flat_on*\/"  */
    yVL_PUBLIC_FLAT_RD = 745,      /* "/\*verilator public_flat_rd*\/"  */
    yVL_PUBLIC_FLAT_RD_ON = 746,   /* "/\*verilator public_flat_rd_on*\/"  */
    yVL_PUBLIC_FLAT_RW = 747,      /* "/\*verilator public_flat_rw*\/"  */
    yVL_PUBLIC_FLAT_RW_ON = 748,   /* "/\*verilator public_flat_rw_on*\/"  */
    yVL_PUBLIC_FLAT_RW_ON_SNS = 749, /* "/\*verilator public_flat_rw_on_sns*\/"  */
    yVL_PUBLIC_ON = 750,           /* "/\*verilator public_on*\/"  */
    yVL_PUBLIC_OFF = 751,          /* "/\*verilator public_off*\/"  */
    yVL_PUBLIC_MODULE = 752,       /* "/\*verilator public_module*\/"  */
    yVL_SC_BV = 753,               /* "/\*verilator sc_bv*\/"  */
    yVL_SFORMAT = 754,             /* "/\*verilator sformat*\/"  */
    yVL_SPLIT_VAR = 755,           /* "/\*verilator split_var*\/"  */
    yVL_TAG = 756,                 /* "/\*verilator tag*\/"  */
    yVL_UNROLL_DISABLE = 757,      /* "/\*verilator unroll_disable*\/"  */
    yVL_UNROLL_FULL = 758,         /* "/\*verilator unroll_full*\/"  */
    yP_TICK = 759,                 /* "'"  */
    yP_TICKBRA = 760,              /* "'{"  */
    yP_OROR = 761,                 /* "||"  */
    yP_ANDAND = 762,               /* "&&"  */
    yP_NOR = 763,                  /* "~|"  */
    yP_XNOR = 764,                 /* "^~"  */
    yP_NAND = 765,                 /* "~&"  */
    yP_EQUAL = 766,                /* "=="  */
    yP_NOTEQUAL = 767,             /* "!="  */
    yP_CASEEQUAL = 768,            /* "==="  */
    yP_CASENOTEQUAL = 769,         /* "!=="  */
    yP_WILDEQUAL = 770,            /* "==?"  */
    yP_WILDNOTEQUAL = 771,         /* "!=?"  */
    yP_GTE = 772,                  /* ">="  */
    yP_LTE = 773,                  /* "<="  */
    yP_LTE__IGNORE = 774,          /* "<=-ignored"  */
    yP_SLEFT = 775,                /* "<<"  */
    yP_SRIGHT = 776,               /* ">>"  */
    yP_SSRIGHT = 777,              /* ">>>"  */
    yP_POW = 778,                  /* "**"  */
    yP_COLON__BEGIN = 779,         /* ":-begin"  */
    yP_COLON__FORK = 780,          /* ":-fork"  */
    yP_PAR__IGNORE = 781,          /* "(-ignored"  */
    yP_PAR__STRENGTH = 782,        /* "(-for-strength"  */
    yP_LTMINUSGT = 783,            /* "<->"  */
    yP_PLUSCOLON = 784,            /* "+:"  */
    yP_MINUSCOLON = 785,           /* "-:"  */
    yP_MINUSGT = 786,              /* "->"  */
    yP_MINUSGTGT = 787,            /* "->>"  */
    yP_EQGT = 788,                 /* "=>"  */
    yP_ASTGT = 789,                /* "*>"  */
    yP_ANDANDAND = 790,            /* "&&&"  */
    yP_POUNDPOUND = 791,           /* "##"  */
    yP_POUNDMINUSPD = 792,         /* "#-#"  */
    yP_POUNDEQPD = 793,            /* "#=#"  */
    yP_DOTSTAR = 794,              /* ".*"  */
    yP_ATAT = 795,                 /* "@@"  */
    yP_COLONCOLON = 796,           /* "::"  */
    yP_COLONEQ = 797,              /* ":="  */
    yP_COLONDIV = 798,             /* ":/"  */
    yP_ORMINUSGT = 799,            /* "|->"  */
    yP_OREQGT = 800,               /* "|=>"  */
    yP_BRASTAR = 801,              /* "[*"  */
    yP_BRAEQ = 802,                /* "[="  */
    yP_BRAMINUSGT = 803,           /* "[->"  */
    yP_BRAPLUSKET = 804,           /* "[+]"  */
    yP_PLUSPLUS = 805,             /* "++"  */
    yP_MINUSMINUS = 806,           /* "--"  */
    yP_PLUSEQ = 807,               /* "+="  */
    yP_MINUSEQ = 808,              /* "-="  */
    yP_TIMESEQ = 809,              /* "*="  */
    yP_DIVEQ = 810,                /* "/="  */
    yP_MODEQ = 811,                /* "%="  */
    yP_ANDEQ = 812,                /* "&="  */
    yP_OREQ = 813,                 /* "|="  */
    yP_XOREQ = 814,                /* "^="  */
    yP_SLEFTEQ = 815,              /* "<<="  */
    yP_SRIGHTEQ = 816,             /* ">>="  */
    yP_SSRIGHTEQ = 817,            /* ">>>="  */
    yP_PLUSSLASHMINUS = 818,       /* "+/-"  */
    yP_PLUSPCTMINUS = 819,         /* "+%-"  */
    prTAGGED = 820,                /* prTAGGED  */
    prPOUNDPOUND_MULTI = 821,      /* prPOUNDPOUND_MULTI  */
    prUNARYARITH = 822,            /* prUNARYARITH  */
    prREDUCTION = 823,             /* prREDUCTION  */
    prNEGATION = 824,              /* prNEGATION  */
    prLOWER_THAN_ELSE = 825        /* prLOWER_THAN_ELSE  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_CONTENT_CAD4U_HDL_VERILATOR_5_024_SRC_V3PARSEBISON_PRETMP_H_INCLUDED  */
