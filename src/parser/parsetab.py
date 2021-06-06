
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ProgDefleftPLUSMINUSleftTIMESDIVIDErightUMINUSAND ARRAY ASSIGNMENT BEGIN BOOLEAN BREAK CASE CHAR COLON COMMA CONST CONTINUE DIGSEQ DIVIDE DO DOTDOT DOWNTO ELSE END ENDPOINT EQ FOR FUNCTION GE GOTO GT ID IF INTEGER INT_NUMBER LBRAC LE LLAVED LLAVEI LPAREN LT MINUS MOD NE NOT OF OR PLUS PROGRAM RBRAC REAL REAL_NUMBER RETURN RPAREN SEMICOLON STRING THEN TIMES TO TYPE USES VAR WHILEBoolExpr : Expr LT ExprExpr : Expr PLUS Exprfunction_definition : function_heading SEMICOLON function_blockBoolExpr : Expr LE ExprExpr : Expr MINUS Exprfunction_definition : emptyVarDef : VAR VarDefList SEMICOLONExpr : Expr TIMES ExprBoolExpr : Expr GT ExprProgDef : PROGRAM ID SEMICOLON SubProg ENDPOINTfunction_heading : FUNCTION funcName COLON return_typeVarDefList : VarDefList SEMICOLON VarDefStateExpr : Expr DIVIDE ExprBoolExpr : Expr GE ExprSubProg : VarDef function_definition compound_statementfunction_heading : FUNCTION funcName parameter_list COLON return_typeVarDefList : VarDefStateExpr : LPAREN Expr RPARENBoolExpr : Expr EQ Exprparameter_list : LPAREN VarDefList RPARENExpr : MINUS Expr %prec UMINUSVarDefState : VarList COLON TypefuncName : IDBoolExpr : Expr NE ExprExpr : VariableVarDefState : ArrayDefStatereturn_type : Typeempty : Expr : constBoolExpr : BoolExpr AND BoolExprVarList : VarList COMMA Variablefunction_block : compound_statementconst : INT_NUMBERVarList : VariableBoolExpr : BoolExpr OR BoolExprconst : REAL_NUMBERlabel_declaration_part : DIGSEQ label_list SEMICOLONArrayDefState : TYPE arrayName EQ ARRAY LBRAC index_list RBRAC OF TypeBoolExpr : NOT BoolExprlabel_declaration_part : emptyarrayName : IDlabel_list : label_list COMMA labelBoolExpr : LPAREN BoolExpr RPARENindex_list : index_list COMMA indexBoolExpr : Exprlabel_list : labelindex_list : indexStateList : StateList SEMICOLON Statementindex : startIndex DOTDOT endIndexStateList : StatementType : INTEGERType : REALStatement : open_statementType : BOOLEANStatement : closed_statementType : arrayNameopen_statement : label COLON non_labeled_open_statementVariable : IDopen_statement : non_labeled_open_statementclosed_statement : label COLON non_labeled_closed_statementstartIndex : constendIndex : constclosed_statement : non_labeled_closed_statementnon_labeled_open_statement : open_if_statementnon_labeled_open_statement : open_while_statementnon_labeled_open_statement : open_for_statementnon_labeled_closed_statement : assignment_statementnon_labeled_closed_statement : compound_statementnon_labeled_closed_statement : closed_if_statementnon_labeled_closed_statement : closed_while_statementnon_labeled_closed_statement : closed_for_statementnon_labeled_closed_statement : goto_statementnon_labeled_closed_statement : emptynon_labeled_closed_statement : case_statementnon_labeled_closed_statement : continue_statementcontinue_statement : CONTINUEnon_labeled_closed_statement : break_statementbreak_statement : BREAKcase_statement : CASE case_index OF case_element_list ENDcase_statement : CASE case_index OF case_element_list SEMICOLON ENDcase_index : Exprcase_element_list : case_element_list SEMICOLON case_elementcase_element_list : case_elementcase_element : case_constant COLON Statementcase_constant : constopen_if_statement : IF BoolExpr THEN Statementopen_if_statement : IF BoolExpr THEN closed_statement ELSE open_statementclosed_if_statement : IF BoolExpr THEN closed_statement ELSE closed_statementopen_while_statement : WHILE BoolExpr DO open_statementclosed_while_statement : WHILE BoolExpr DO closed_statementopen_for_statement : FOR Variable ASSIGNMENT initial_value direction final_value DO open_statementclosed_for_statement : FOR Variable ASSIGNMENT initial_value direction final_value DO closed_statementinitial_value : Exprfinal_value : Exprdirection : TOdirection : DOWNTOassignment_statement : Variable ASSIGNMENT Exprcompound_statement : BEGIN StateList ENDgoto_statement : GOTO labellabel : DIGSEQ'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,8,],[0,-10,]),'ID':([2,7,12,18,21,25,26,27,51,52,53,56,61,63,73,74,77,78,79,86,90,93,99,100,101,102,103,104,105,106,107,108,109,110,111,116,117,123,125,129,130,158,159,162,163,164,167,171,174,175,181,187,189,190,194,],[3,19,24,29,19,19,29,19,19,19,19,19,29,19,19,19,19,19,19,19,19,29,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-95,-96,19,19,19,19,29,19,19,19,19,]),'SEMICOLON':([3,10,13,14,16,19,21,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,57,58,64,65,66,67,68,69,72,73,74,80,81,82,83,87,91,92,94,96,97,98,99,115,116,118,121,126,127,139,140,141,142,144,145,146,149,150,158,159,165,167,171,172,173,174,178,179,180,185,187,188,189,191,192,194,],[4,22,25,-17,-26,-58,-28,-41,73,-50,-53,-55,-59,-63,-100,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-77,-76,-78,-12,-22,-51,-52,-54,-56,-98,-28,-28,-25,-29,-33,-36,-99,-11,-27,123,-48,-57,-60,-28,-21,-28,-97,-16,-86,-55,-2,-5,-8,-13,-18,-89,-90,166,-83,-28,-28,-79,-28,-28,-88,-87,-28,-80,-82,-84,-55,-28,-38,-28,-91,-92,-28,]),'VAR':([4,],[7,]),'ENDPOINT':([5,20,72,],[8,-15,-98,]),'FUNCTION':([6,25,],[12,-7,]),'BEGIN':([6,9,11,21,22,25,59,60,72,73,74,99,116,158,159,167,171,174,187,189,194,],[-28,21,-6,21,21,-7,-3,-32,-98,21,21,21,21,21,21,21,21,21,21,21,21,]),'TYPE':([7,25,63,123,],[18,18,18,18,]),'RPAREN':([14,16,19,29,64,65,66,67,68,69,76,80,81,82,83,94,112,113,114,115,120,131,132,133,134,135,136,137,138,139,140,141,142,143,144,188,],[-17,-26,-58,-41,-12,-22,-51,-52,-54,-56,-45,-25,-29,-33,-36,122,-39,143,144,-21,144,-30,-35,-1,-4,-9,-14,-19,-24,-2,-5,-8,-13,-43,-18,-38,]),'COLON':([15,17,19,23,24,34,37,62,70,82,83,122,128,151,152,],[26,-34,-58,61,-23,74,-100,93,-31,-33,-36,-20,159,167,-85,]),'COMMA':([15,17,19,70,82,83,153,154,182,183,184,],[27,-34,-58,-31,-33,-36,169,-47,-44,-49,-62,]),'ASSIGNMENT':([19,54,85,161,],[-58,86,117,175,]),'LT':([19,76,80,81,82,83,114,115,139,140,141,142,144,],[-58,102,-25,-29,-33,-36,102,-21,-2,-5,-8,-13,-18,]),'LE':([19,76,80,81,82,83,114,115,139,140,141,142,144,],[-58,103,-25,-29,-33,-36,103,-21,-2,-5,-8,-13,-18,]),'GT':([19,76,80,81,82,83,114,115,139,140,141,142,144,],[-58,104,-25,-29,-33,-36,104,-21,-2,-5,-8,-13,-18,]),'GE':([19,76,80,81,82,83,114,115,139,140,141,142,144,],[-58,105,-25,-29,-33,-36,105,-21,-2,-5,-8,-13,-18,]),'EQ':([19,28,29,76,80,81,82,83,114,115,139,140,141,142,144,],[-58,71,-41,106,-25,-29,-33,-36,106,-21,-2,-5,-8,-13,-18,]),'NE':([19,76,80,81,82,83,114,115,139,140,141,142,144,],[-58,107,-25,-29,-33,-36,107,-21,-2,-5,-8,-13,-18,]),'PLUS':([19,76,80,81,82,83,89,114,115,118,120,133,134,135,136,137,138,139,140,141,142,144,148,177,],[-58,108,-25,-29,-33,-36,108,108,-21,108,108,108,108,108,108,108,108,-2,-5,-8,-13,-18,108,108,]),'MINUS':([19,51,52,56,76,77,78,79,80,81,82,83,86,89,90,100,101,102,103,104,105,106,107,108,109,110,111,114,115,117,118,120,125,129,133,134,135,136,137,138,139,140,141,142,144,148,162,163,164,175,177,190,],[-58,79,79,79,109,79,79,79,-25,-29,-33,-36,79,109,79,79,79,79,79,79,79,79,79,79,79,79,79,109,-21,79,109,109,79,79,109,109,109,109,109,109,-2,-5,-8,-13,-18,109,79,-95,-96,79,109,79,]),'TIMES':([19,76,80,81,82,83,89,114,115,118,120,133,134,135,136,137,138,139,140,141,142,144,148,177,],[-58,110,-25,-29,-33,-36,110,110,-21,110,110,110,110,110,110,110,110,110,110,-8,-13,-18,110,110,]),'DIVIDE':([19,76,80,81,82,83,89,114,115,118,120,133,134,135,136,137,138,139,140,141,142,144,148,177,],[-58,111,-25,-29,-33,-36,111,111,-21,111,111,111,111,111,111,111,111,111,111,-8,-13,-18,111,111,]),'THEN':([19,75,76,80,81,82,83,112,115,131,132,133,134,135,136,137,138,139,140,141,142,143,144,157,],[-58,99,-45,-25,-29,-33,-36,-39,-21,-30,-35,-1,-4,-9,-14,-19,-24,-2,-5,-8,-13,-43,-18,171,]),'AND':([19,75,76,80,81,82,83,84,112,113,114,115,131,132,133,134,135,136,137,138,139,140,141,142,143,144,157,160,],[-58,100,-45,-25,-29,-33,-36,100,100,100,-45,-21,100,100,-1,-4,-9,-14,-19,-24,-2,-5,-8,-13,-43,-18,100,100,]),'OR':([19,75,76,80,81,82,83,84,112,113,114,115,131,132,133,134,135,136,137,138,139,140,141,142,143,144,157,160,],[-58,101,-45,-25,-29,-33,-36,101,101,101,-45,-21,101,101,-1,-4,-9,-14,-19,-24,-2,-5,-8,-13,-43,-18,101,101,]),'DO':([19,76,80,81,82,83,84,112,115,131,132,133,134,135,136,137,138,139,140,141,142,143,144,160,176,177,193,],[-58,-45,-25,-29,-33,-36,116,-39,-21,-30,-35,-1,-4,-9,-14,-19,-24,-2,-5,-8,-13,-43,-18,174,187,-94,194,]),'OF':([19,80,81,82,83,88,89,115,139,140,141,142,144,168,],[-58,-25,-29,-33,-36,119,-81,-21,-2,-5,-8,-13,-18,181,]),'END':([19,21,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,57,58,72,73,74,80,81,82,83,87,96,97,98,99,115,116,118,126,127,139,140,141,142,144,145,146,149,150,158,159,165,166,167,171,172,173,174,178,179,180,185,187,189,191,192,194,],[-58,-28,72,-50,-53,-55,-59,-63,-100,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-77,-76,-78,-98,-28,-28,-25,-29,-33,-36,-99,-48,-57,-60,-28,-21,-28,-97,-86,-55,-2,-5,-8,-13,-18,-89,-90,165,-83,-28,-28,-79,178,-28,-28,-88,-87,-28,-80,-82,-84,-55,-28,-28,-91,-92,-28,]),'ELSE':([19,36,37,41,42,43,44,45,46,47,48,49,50,57,58,72,74,80,81,82,83,87,98,99,115,116,118,127,139,140,141,142,144,146,158,159,165,171,172,174,178,185,187,189,192,194,],[-58,-63,-100,-67,-68,-69,-70,-71,-72,-73,-74,-75,-77,-76,-78,-98,-28,-25,-29,-33,-36,-99,-60,-28,-21,-28,-97,158,-2,-5,-8,-13,-18,-90,-28,-28,-79,-28,-88,-28,-80,189,-28,-28,-92,-28,]),'TO':([19,80,81,82,83,115,139,140,141,142,144,147,148,186,],[-58,-25,-29,-33,-36,-21,-2,-5,-8,-13,-18,163,-93,163,]),'DOWNTO':([19,80,81,82,83,115,139,140,141,142,144,147,148,186,],[-58,-25,-29,-33,-36,-21,-2,-5,-8,-13,-18,164,-93,164,]),'DIGSEQ':([21,55,73,99,116,158,167,171,174,187,189,194,],[37,37,37,37,37,37,37,37,37,37,37,37,]),'IF':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[51,51,51,125,51,51,125,51,125,125,51,125,125,]),'WHILE':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[52,52,52,129,52,52,129,52,129,129,52,129,129,]),'FOR':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[53,53,53,130,53,53,130,53,130,130,53,130,130,]),'GOTO':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[55,55,55,55,55,55,55,55,55,55,55,55,55,]),'CASE':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[56,56,56,56,56,56,56,56,56,56,56,56,56,]),'CONTINUE':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[57,57,57,57,57,57,57,57,57,57,57,57,57,]),'BREAK':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[58,58,58,58,58,58,58,58,58,58,58,58,58,]),'LPAREN':([23,24,51,52,56,77,78,79,86,90,100,101,102,103,104,105,106,107,108,109,110,111,117,125,129,162,163,164,175,190,],[63,-23,78,78,90,78,78,90,90,90,78,78,90,90,90,90,90,90,90,90,90,90,90,78,78,90,-95,-96,90,90,]),'INTEGER':([26,61,93,181,],[66,66,66,66,]),'REAL':([26,61,93,181,],[67,67,67,67,]),'BOOLEAN':([26,61,93,181,],[68,68,68,68,]),'NOT':([51,52,77,78,100,101,125,129,],[77,77,77,77,77,77,77,77,]),'INT_NUMBER':([51,52,56,77,78,79,86,90,100,101,102,103,104,105,106,107,108,109,110,111,117,119,124,125,129,162,163,164,166,169,170,175,190,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,-95,-96,82,82,82,82,82,]),'REAL_NUMBER':([51,52,56,77,78,79,86,90,100,101,102,103,104,105,106,107,108,109,110,111,117,119,124,125,129,162,163,164,166,169,170,175,190,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,-95,-96,83,83,83,83,83,]),'ARRAY':([71,],[95,]),'DOTDOT':([82,83,155,156,],[-33,-36,170,-61,]),'RBRAC':([82,83,153,154,182,183,184,],[-33,-36,168,-47,-44,-49,-62,]),'LBRAC':([95,],[124,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ProgDef':([0,],[1,]),'SubProg':([4,],[5,]),'VarDef':([4,],[6,]),'function_definition':([6,],[9,]),'function_heading':([6,],[10,]),'empty':([6,21,73,74,99,116,158,159,167,171,174,187,189,194,],[11,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'VarDefList':([7,63,],[13,94,]),'VarDefState':([7,25,63,123,],[14,64,14,64,]),'VarList':([7,25,63,123,],[15,15,15,15,]),'ArrayDefState':([7,25,63,123,],[16,16,16,16,]),'Variable':([7,21,25,27,51,52,53,56,63,73,74,77,78,79,86,90,99,100,101,102,103,104,105,106,107,108,109,110,111,116,117,123,125,129,130,158,159,162,167,171,174,175,187,189,190,194,],[17,54,17,70,80,80,85,80,17,54,54,80,80,80,80,80,54,80,80,80,80,80,80,80,80,80,80,80,80,54,80,17,80,80,161,54,54,80,54,54,54,80,54,54,80,54,]),'compound_statement':([9,21,22,73,74,99,116,158,159,167,171,174,187,189,194,],[20,42,60,42,42,42,42,42,42,42,42,42,42,42,42,]),'funcName':([12,],[23,]),'arrayName':([18,26,61,93,181,],[28,69,69,69,69,]),'StateList':([21,],[30,]),'Statement':([21,73,99,167,171,],[31,96,126,180,126,]),'open_statement':([21,73,99,116,158,167,171,174,187,189,194,],[32,32,32,145,173,32,32,145,191,173,191,]),'closed_statement':([21,73,99,116,158,167,171,174,187,189,194,],[33,33,127,146,172,33,185,146,192,172,192,]),'label':([21,55,73,99,116,158,167,171,174,187,189,194,],[34,87,34,128,34,34,34,128,128,34,128,128,]),'non_labeled_open_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[35,35,97,35,35,35,97,35,35,35,35,35,35,]),'non_labeled_closed_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[36,36,98,36,36,36,98,36,36,36,36,36,36,]),'open_if_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[38,38,38,38,38,38,38,38,38,38,38,38,38,]),'open_while_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[39,39,39,39,39,39,39,39,39,39,39,39,39,]),'open_for_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[40,40,40,40,40,40,40,40,40,40,40,40,40,]),'assignment_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[41,41,41,41,41,41,41,41,41,41,41,41,41,]),'closed_if_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[43,43,43,43,43,43,43,43,43,43,43,43,43,]),'closed_while_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[44,44,44,44,44,44,44,44,44,44,44,44,44,]),'closed_for_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[45,45,45,45,45,45,45,45,45,45,45,45,45,]),'goto_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[46,46,46,46,46,46,46,46,46,46,46,46,46,]),'case_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[48,48,48,48,48,48,48,48,48,48,48,48,48,]),'continue_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[49,49,49,49,49,49,49,49,49,49,49,49,49,]),'break_statement':([21,73,74,99,116,158,159,167,171,174,187,189,194,],[50,50,50,50,50,50,50,50,50,50,50,50,50,]),'function_block':([22,],[59,]),'parameter_list':([23,],[62,]),'Type':([26,61,93,181,],[65,92,92,188,]),'BoolExpr':([51,52,77,78,100,101,125,129,],[75,84,112,113,131,132,157,160,]),'Expr':([51,52,56,77,78,79,86,90,100,101,102,103,104,105,106,107,108,109,110,111,117,125,129,162,175,190,],[76,76,89,76,114,115,118,120,76,76,133,134,135,136,137,138,139,140,141,142,148,76,76,177,148,177,]),'const':([51,52,56,77,78,79,86,90,100,101,102,103,104,105,106,107,108,109,110,111,117,119,124,125,129,162,166,169,170,175,190,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,152,156,81,81,81,152,156,184,81,81,]),'case_index':([56,],[88,]),'return_type':([61,93,],[91,121,]),'initial_value':([117,175,],[147,186,]),'case_element_list':([119,],[149,]),'case_element':([119,166,],[150,179,]),'case_constant':([119,166,],[151,151,]),'index_list':([124,],[153,]),'index':([124,169,],[154,182,]),'startIndex':([124,169,],[155,155,]),'direction':([147,186,],[162,190,]),'final_value':([162,190,],[176,193,]),'endIndex':([170,],[183,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ProgDef","S'",1,None,None,None),
  ('BoolExpr -> Expr LT Expr','BoolExpr',3,'p_BoolExpr_LT','bool.py',10),
  ('Expr -> Expr PLUS Expr','Expr',3,'p_expression_plus','expression.py',11),
  ('function_definition -> function_heading SEMICOLON function_block','function_definition',3,'p_function_definition_1','function.py',16),
  ('BoolExpr -> Expr LE Expr','BoolExpr',3,'p_BoolExpr_LE','bool.py',17),
  ('Expr -> Expr MINUS Expr','Expr',3,'p_expression_minus','expression.py',17),
  ('function_definition -> empty','function_definition',1,'p_function_definition_2','function.py',22),
  ('VarDef -> VAR VarDefList SEMICOLON','VarDef',3,'p_VarDef','var_def.py',22),
  ('Expr -> Expr TIMES Expr','Expr',3,'p_expression_times','expression.py',23),
  ('BoolExpr -> Expr GT Expr','BoolExpr',3,'p_BoolExpr_GT','bool.py',24),
  ('ProgDef -> PROGRAM ID SEMICOLON SubProg ENDPOINT','ProgDef',5,'p_ProgDef','parser.py',25),
  ('function_heading -> FUNCTION funcName COLON return_type','function_heading',4,'p_function_heading_1','function.py',27),
  ('VarDefList -> VarDefList SEMICOLON VarDefState','VarDefList',3,'p_VarDefList_1','var_def.py',28),
  ('Expr -> Expr DIVIDE Expr','Expr',3,'p_expression_div','expression.py',29),
  ('BoolExpr -> Expr GE Expr','BoolExpr',3,'p_BoolExpr_GE','bool.py',31),
  ('SubProg -> VarDef function_definition compound_statement','SubProg',3,'p_SubProg','parser.py',31),
  ('function_heading -> FUNCTION funcName parameter_list COLON return_type','function_heading',5,'p_function_heading_2','function.py',33),
  ('VarDefList -> VarDefState','VarDefList',1,'p_VarDefList_2','var_def.py',34),
  ('Expr -> LPAREN Expr RPAREN','Expr',3,'p_expr_Parentheses','expression.py',35),
  ('BoolExpr -> Expr EQ Expr','BoolExpr',3,'p_BoolExpr_EQ','bool.py',38),
  ('parameter_list -> LPAREN VarDefList RPAREN','parameter_list',3,'p_parameter_list','function.py',39),
  ('Expr -> MINUS Expr','Expr',2,'p_expression_uminus','expression.py',40),
  ('VarDefState -> VarList COLON Type','VarDefState',3,'p_VarDefState_1','var_def.py',40),
  ('funcName -> ID','funcName',1,'p_funcName','function.py',44),
  ('BoolExpr -> Expr NE Expr','BoolExpr',3,'p_BoolExpr_NE','bool.py',45),
  ('Expr -> Variable','Expr',1,'p_expression_variable','expression.py',46),
  ('VarDefState -> ArrayDefState','VarDefState',1,'p_VarDefState_2','var_def.py',46),
  ('return_type -> Type','return_type',1,'p_return_type','function.py',49),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',49),
  ('Expr -> const','Expr',1,'p_expression_const','expression.py',51),
  ('BoolExpr -> BoolExpr AND BoolExpr','BoolExpr',3,'p_BoolExpr_AND','bool.py',52),
  ('VarList -> VarList COMMA Variable','VarList',3,'p_VarList_1','var_def.py',52),
  ('function_block -> compound_statement','function_block',1,'p_function_block','function.py',54),
  ('const -> INT_NUMBER','const',1,'p_const_INT_NUMBER','expression.py',57),
  ('VarList -> Variable','VarList',1,'p_VarList_2','var_def.py',58),
  ('BoolExpr -> BoolExpr OR BoolExpr','BoolExpr',3,'p_BoolExpr_OR','bool.py',59),
  ('const -> REAL_NUMBER','const',1,'p_const_REAL_NUMBER','expression.py',62),
  ('label_declaration_part -> DIGSEQ label_list SEMICOLON','label_declaration_part',3,'p_label_declaration_part_1','parser.py',62),
  ('ArrayDefState -> TYPE arrayName EQ ARRAY LBRAC index_list RBRAC OF Type','ArrayDefState',9,'p_ArrayDefState','var_def.py',64),
  ('BoolExpr -> NOT BoolExpr','BoolExpr',2,'p_BoolExpr_NOT','bool.py',66),
  ('label_declaration_part -> empty','label_declaration_part',1,'p_label_declaration_part_2','parser.py',67),
  ('arrayName -> ID','arrayName',1,'p_arrayName','var_def.py',70),
  ('label_list -> label_list COMMA label','label_list',3,'p_label_list_1','parser.py',72),
  ('BoolExpr -> LPAREN BoolExpr RPAREN','BoolExpr',3,'p_BoolExpr_Parentheses','bool.py',73),
  ('index_list -> index_list COMMA index','index_list',3,'p_index_list_1','var_def.py',76),
  ('BoolExpr -> Expr','BoolExpr',1,'p_BoolExpr','bool.py',78),
  ('label_list -> label','label_list',1,'p_label_list_2','parser.py',78),
  ('index_list -> index','index_list',1,'p_index_list_2','var_def.py',82),
  ('StateList -> StateList SEMICOLON Statement','StateList',3,'p_statementList_1','statement.py',88),
  ('index -> startIndex DOTDOT endIndex','index',3,'p_index','var_def.py',88),
  ('StateList -> Statement','StateList',1,'p_statementList_2','statement.py',94),
  ('Type -> INTEGER','Type',1,'p_type_1','var_def.py',94),
  ('Type -> REAL','Type',1,'p_type_2','var_def.py',99),
  ('Statement -> open_statement','Statement',1,'p_statement_1','statement.py',100),
  ('Type -> BOOLEAN','Type',1,'p_type_3','var_def.py',104),
  ('Statement -> closed_statement','Statement',1,'p_statement_2','statement.py',105),
  ('Type -> arrayName','Type',1,'p_type_4','var_def.py',109),
  ('open_statement -> label COLON non_labeled_open_statement','open_statement',3,'p_open_statement_1','statement.py',110),
  ('Variable -> ID','Variable',1,'p_variable_id','var_def.py',114),
  ('open_statement -> non_labeled_open_statement','open_statement',1,'p_open_statement_2','statement.py',116),
  ('closed_statement -> label COLON non_labeled_closed_statement','closed_statement',3,'p_closed_statement_1','statement.py',121),
  ('startIndex -> const','startIndex',1,'p_startIndex','var_def.py',121),
  ('endIndex -> const','endIndex',1,'p_endIndex','var_def.py',126),
  ('closed_statement -> non_labeled_closed_statement','closed_statement',1,'p_closed_statement_2','statement.py',127),
  ('non_labeled_open_statement -> open_if_statement','non_labeled_open_statement',1,'p_non_labeled_open_statement_1','statement.py',132),
  ('non_labeled_open_statement -> open_while_statement','non_labeled_open_statement',1,'p_non_labeled_open_statement_2','statement.py',137),
  ('non_labeled_open_statement -> open_for_statement','non_labeled_open_statement',1,'p_non_labeled_open_statement_3','statement.py',142),
  ('non_labeled_closed_statement -> assignment_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_1','statement.py',147),
  ('non_labeled_closed_statement -> compound_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_2','statement.py',153),
  ('non_labeled_closed_statement -> closed_if_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_3','statement.py',159),
  ('non_labeled_closed_statement -> closed_while_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_4','statement.py',165),
  ('non_labeled_closed_statement -> closed_for_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_5','statement.py',171),
  ('non_labeled_closed_statement -> goto_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_6','statement.py',177),
  ('non_labeled_closed_statement -> empty','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_7','statement.py',183),
  ('non_labeled_closed_statement -> case_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_8','statement.py',189),
  ('non_labeled_closed_statement -> continue_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_9','statement.py',195),
  ('continue_statement -> CONTINUE','continue_statement',1,'p_continue_statement','statement.py',200),
  ('non_labeled_closed_statement -> break_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_10','statement.py',206),
  ('break_statement -> BREAK','break_statement',1,'p_break_statement','statement.py',211),
  ('case_statement -> CASE case_index OF case_element_list END','case_statement',5,'p_case_statement_1','statement.py',225),
  ('case_statement -> CASE case_index OF case_element_list SEMICOLON END','case_statement',6,'p_case_statement_2','statement.py',231),
  ('case_index -> Expr','case_index',1,'p_case_index','statement.py',237),
  ('case_element_list -> case_element_list SEMICOLON case_element','case_element_list',3,'p_case_element_list_1','statement.py',242),
  ('case_element_list -> case_element','case_element_list',1,'p_case_element_list_2','statement.py',248),
  ('case_element -> case_constant COLON Statement','case_element',3,'p_case_element','statement.py',254),
  ('case_constant -> const','case_constant',1,'p_case_constant','statement.py',260),
  ('open_if_statement -> IF BoolExpr THEN Statement','open_if_statement',4,'p_open_if_statement_1','statement.py',265),
  ('open_if_statement -> IF BoolExpr THEN closed_statement ELSE open_statement','open_if_statement',6,'p_open_if_statement_2','statement.py',271),
  ('closed_if_statement -> IF BoolExpr THEN closed_statement ELSE closed_statement','closed_if_statement',6,'p_closed_if_statement','statement.py',277),
  ('open_while_statement -> WHILE BoolExpr DO open_statement','open_while_statement',4,'p_open_while_statement','statement.py',283),
  ('closed_while_statement -> WHILE BoolExpr DO closed_statement','closed_while_statement',4,'p_closed_while_statement','statement.py',289),
  ('open_for_statement -> FOR Variable ASSIGNMENT initial_value direction final_value DO open_statement','open_for_statement',8,'p_open_for_statement','statement.py',295),
  ('closed_for_statement -> FOR Variable ASSIGNMENT initial_value direction final_value DO closed_statement','closed_for_statement',8,'p_closed_for_statement','statement.py',301),
  ('initial_value -> Expr','initial_value',1,'p_initial_value','statement.py',307),
  ('final_value -> Expr','final_value',1,'p_final_value','statement.py',312),
  ('direction -> TO','direction',1,'p_direction_1','statement.py',317),
  ('direction -> DOWNTO','direction',1,'p_direction_2','statement.py',322),
  ('assignment_statement -> Variable ASSIGNMENT Expr','assignment_statement',3,'p_assignment_statement','statement.py',327),
  ('compound_statement -> BEGIN StateList END','compound_statement',3,'p_compound_statement','statement.py',333),
  ('goto_statement -> GOTO label','goto_statement',2,'p_goto_statement','statement.py',341),
  ('label -> DIGSEQ','label',1,'p_label','statement.py',347),
]
