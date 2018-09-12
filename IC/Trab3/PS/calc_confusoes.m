function matriz_conf= calc_confusoes(real,pred)
    
    
if(size(real)~= size(pred))
    error('incoherent number of solutions');
end

[Numofcases dummy]=size(real);

%% Real Psoriasis 
Pp_p= sum(sum((real==1)&(pred==1)))/sum(sum((real==1)));
Pp_sd=sum(sum((real==1)&(pred==2)))/sum(sum((real==1)));
Pp_lp=sum(sum((real==1)&(pred==3)))/sum(sum((real==1)));
Pp_pr=sum(sum((real==1)&(pred==4)))/sum(sum((real==1)));
Pp_cd=sum(sum((real==1)&(pred==5)))/sum(sum((real==1)));
Pp_prp=sum(sum((real==1)&(pred==6)))/sum(sum((real==1)));

%% Real seboreic dermatitis
Psd_p=sum(sum((real==2)&(pred==1)))/sum(sum((real==2)));
Psd_sd=sum(sum((real==2)&(pred==2)))/sum(sum((real==2)));
Psd_lp=sum(sum((real==2)&(pred==3)))/sum(sum((real==2)));
Psd_pr=sum(sum((real==2)&(pred==4)))/sum(sum((real==2)));
Psd_cd=sum(sum((real==2)&(pred==5)))/sum(sum((real==2)));
Psd_prp=sum(sum((real==2)&(pred==6)))/sum(sum((real==2)));
%% Real lichen planus 
Plp_p=sum(sum((real==3)&(pred==1)))/sum(sum((real==3)));
Plp_sd=sum(sum((real==3)&(pred==2)))/sum(sum((real==3)));
Plp_lp=sum(sum((real==3)&(pred==3)))/sum(sum((real==3)));
Plp_pr=sum(sum((real==3)&(pred==4)))/sum(sum((real==3)));
Plp_cd=sum(sum((real==3)&(pred==5)))/sum(sum((real==3)));
Plp_prp=sum(sum((real==3)&(pred==6)))/sum(sum((real==3)));
%% Real pityriasis rosea 
Ppr_p=sum( sum((real==4)&(pred==1)))/sum(sum((real==4)));
Ppr_sd=sum(sum((real==4)&(pred==2)))/sum(sum((real==4)));
Ppr_lp=sum(sum((real==4)&(pred==3)))/sum(sum((real==4)));
Ppr_pr=sum(sum((real==4)&(pred==4)))/sum(sum((real==4)));
Ppr_cd=sum(sum((real==4)&(pred==5)))/sum(sum((real==4)));
Ppr_prp=sum(sum((real==4)&(pred==6)))/sum(sum((real==4)));
%% Real cronic dermatitis
Pcd_p= sum(sum((real==5)&(pred==1)))/sum(sum((real==5)));
Pcd_sd=sum(sum((real==5)&(pred==2)))/sum(sum((real==5)));
Pcd_lp=sum(sum((real==5)&(pred==3)))/sum(sum((real==5)));
Pcd_pr=sum(sum((real==5)&(pred==4)))/sum(sum((real==5)));
Pcd_cd=sum(sum((real==5)&(pred==5)))/sum(sum((real==5)));
Pcd_prp=sum(sum((real==5)&(pred==6)))/sum(sum((real==5)));
%% Real pityriasis rubra pilaris 
Pprp_p= sum(sum((real==6)&(pred==1)))/sum(sum((real==6)));
Pprp_sd=sum(sum((real==6)&(pred==2)))/sum(sum((real==6)));
Pprp_lp=sum(sum((real==6)&(pred==3)))/sum(sum((real==6)));
Pprp_pr=sum(sum((real==6)&(pred==4)))/sum(sum((real==6)));
Pprp_cd=sum(sum((real==6)&(pred==5)))/sum(sum((real==6)));
Pprp_prp=sum(sum((real==6)&(pred==6)))/sum(sum((real==6)));

matriz_conf=[ Pp_p,Pp_sd, Pp_lp,Pp_pr,Pp_cd,Pp_prp;...
              Psd_p,Psd_sd, Psd_lp,Psd_pr,Psd_cd,Psd_prp;...
              Plp_p,Plp_sd, Plp_lp,Plp_pr,Plp_cd,Plp_prp;...
              Ppr_p,Ppr_sd, Ppr_lp,Ppr_pr,Ppr_cd,Ppr_prp;...
              Pcd_p,Pcd_sd, Pcd_lp,Pcd_pr,Pcd_cd,Pcd_prp;...
              Pprp_p,Pprp_sd, Pprp_lp,Pprp_pr,Pprp_cd,Pprp_prp];
end