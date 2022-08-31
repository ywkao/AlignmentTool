//void DrawPredictedHits( TFile* f, TString outputStem )
void DrawHits( TString rootfile, TString outputStem )
{
    TFile* f = new TFile(rootfile);

	TTree* t = (TTree*)f->Get("ESAlignmentTool/tree");
	TH2D* mf = new TH2D("h_mf","-Front;x[cm];y[cm]",250,-125,125,250,-125,125);
	TH2D* mr = new TH2D("h_mr","-Rear;x[cm];y[cm]",250,-125,125,250,-125,125);
	TH2D* pf = new TH2D("h_pf","+Front;x[cm];y[cm]",250,-125,125,250,-125,125);
	TH2D* pr = new TH2D("h_pr","+Rear;x[cm];y[cm]",250,-125,125,250,-125,125);

	const int nHits = 2000;
	const int nZ = 2; // +/-, 0=-, 1=+
	const int nP = 2; // R/F, 0=F, 1=R

	double ES_O_X[2][2],ES_O_Y[2][2],ES_O_Z[2][2];
	double ES_O_R11[2][2],ES_O_R12[2][2],ES_O_R13[2][2];
 	double ES_O_R21[2][2],ES_O_R22[2][2],ES_O_R23[2][2];
 	double ES_O_R31[2][2],ES_O_R32[2][2],ES_O_R33[2][2];

    //Aligned, P-dP
	ES_O_X[0][0]=0.165197;ES_O_Y[0][0]=-0.655798; ES_O_Z[0][0]=-304.393;
	ES_O_X[0][1]=0.160553;ES_O_Y[0][1]=-0.648491; ES_O_Z[0][1]=-309.023;
	ES_O_X[1][0]=0.260936; 	ES_O_Y[1][0]=-0.696511; 	ES_O_Z[1][0]=304.251;
	ES_O_X[1][1]=0.26097; 	ES_O_Y[1][1]=-0.665503; ES_O_Z[1][1]=308.863;

    //ESmF_O_R:
	ES_O_R11[0][0]=1            ; ES_O_R12[0][0]=5.60311e-05  ; ES_O_R13[0][0]=-0.00053569  ;
	ES_O_R21[0][0]=-5.55953e-05 ; ES_O_R22[0][0]=1            ; ES_O_R23[0][0]=0.000832029  ;
	ES_O_R31[0][0]=0.000535736  ; ES_O_R32[0][0]=-0.000832    ; ES_O_R33[0][0]=1            ;

    //ESmR_O_R:
	ES_O_R11[0][1]=1            ; ES_O_R12[0][1]=-0.000440656 ; ES_O_R13[0][1]=-0.000343017 ;
	ES_O_R21[0][1]=0.000441024  ; ES_O_R22[0][1]=0.999999     ; ES_O_R23[0][1]=0.00107226   ;
	ES_O_R31[0][1]=0.000342544  ; ES_O_R32[0][1]=-0.00107241  ; ES_O_R33[0][1]=0.999999     ;

    //ESpF_O_R:
	ES_O_R11[1][0]=0.999999     ; ES_O_R12[1][0]=0.00154597   ; ES_O_R13[1][0]=-2.53903e-05 ;
	ES_O_R21[1][0]=-0.001546    ; ES_O_R22[1][0]=0.999998     ; ES_O_R23[1][0]=-0.00103888  ;
	ES_O_R31[1][0]=2.37842e-05  ; ES_O_R32[1][0]=0.00103892   ; ES_O_R33[1][0]=0.999999     ;

    //ESpR_O_R:
	ES_O_R11[1][1]=0.999999     ; ES_O_R12[1][1]=0.0013284    ; ES_O_R13[1][1]=-0.000256246 ;
	ES_O_R21[1][1]=-0.00132871  ; ES_O_R22[1][1]=0.999998     ; ES_O_R23[1][1]=-0.00118935  ;
	ES_O_R31[1][1]=0.000254665  ; ES_O_R32[1][1]=0.00118969   ; ES_O_R33[1][1]=0.999999     ;

	int Ntrack;
	double PredictionState_X[nHits][nZ][nP];
	double PredictionState_Y[nHits][nZ][nP];
	double PredictionState_Z[nHits][nZ][nP];
	t->SetBranchAddress("Ntrack", &Ntrack);
	t->SetBranchAddress("PredictionState_X", &PredictionState_X[0][0][0]);	
	t->SetBranchAddress("PredictionState_Y", &PredictionState_Y[0][0][0]);	
	t->SetBranchAddress("PredictionState_Z", &PredictionState_Z[0][0][0]);

	cout<<"Total events: "<<t->GetEntries()<<endl;
	for( int entry=0; entry<t->GetEntries(); entry++ )	
	{
		if( entry%100 == 0 ) cout<<".";
		t->GetEntry(entry);
		for( int itrk=0; itrk<Ntrack; itrk++){
			double X[nZ][nP];
			double Y[nZ][nP];
			for( int z=0; z<2; z++){
				for( int p=0; p<2; p++)
				{
					X[z][p]= (PredictionState_X[itrk][z][p]-ES_O_X[z][p])*ES_O_R11[z][p]
					        +(PredictionState_Y[itrk][z][p]-ES_O_Y[z][p])*ES_O_R12[z][p]
					        +(PredictionState_Z[itrk][z][p]-ES_O_Z[z][p])*ES_O_R13[z][p];
					Y[z][p]= (PredictionState_X[itrk][z][p]-ES_O_X[z][p])*ES_O_R21[z][p]
					        +(PredictionState_Y[itrk][z][p]-ES_O_Y[z][p])*ES_O_R22[z][p]
					        +(PredictionState_Z[itrk][z][p]-ES_O_Z[z][p])*ES_O_R23[z][p];
				}
			}
			mf->Fill(X[0][0],Y[0][0]);
			mr->Fill(X[0][1],Y[0][1]);
			pf->Fill(X[1][0],Y[1][0]);
			pr->Fill(X[1][1],Y[1][0]);
		}
	}
	cout<<endl<<"End"<<endl;	
	TCanvas* c1 = new TCanvas("4 plots", "", 1000, 800);
	c1->Divide(2,2);
	c1->cd(1);
	mf->Draw("COLZ");
	c1->cd(2);
	mr->Draw("COLZ");
	c1->cd(3);
	pf->Draw("COLZ");
	c1->cd(4);
	pr->Draw("COLZ");
    c1->SaveAs(("./eos/"+outputStem+".png").Data());
    c1->SaveAs(("./eos/"+outputStem+".pdf").Data());
}
