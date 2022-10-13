using namespace std;
void fitResidual(TH1D* h1, string xName, float xrange=3, Color_t color=2){
    TF1* gaus1_ = new TF1("gaus1_","gaus", -1*xrange, xrange );
    gaus1_->SetLineColor(color); 
    h1->Fit("gaus1_","WR"); cout<<endl;
    double Mean = gaus1_->GetParameter(1);
    double Width = gaus1_->GetParameter(2);
    gaus1_->SetRange(Mean-1.5*Width,Mean+1.5*Width);
    h1->Fit("gaus1_", "WR");
    h1->SetXTitle(xName.c_str());
    h1->SetYTitle("Yields");
}

void setStyle( TH1D* h1){
    h1->SetMarkerColor(1);
    h1->SetMarkerStyle(20);
    h1->SetMarkerSize(0.6);
}

void setStyle( TH1D* h1, int color, int style){
    h1->GetXaxis()->SetTitleSize(0.06);
    h1->GetYaxis()->SetTitleSize(0.06);
    h1->GetYaxis()->SetTitle("Yields");

    h1->SetMarkerColor(color);
    h1->SetMarkerStyle(style);
    h1->SetMarkerSize(0.6);
}

void annotate(){
    TLatex latex;
    latex.SetNDC();
    latex.SetTextFont(43);
    latex.SetTextAlign(11);
    latex.SetTextSize(16);
    latex.DrawLatex(0.18, 0.965, "#bf{CMS} #it{Preliminary}");
    latex.DrawLatex(0.68, 0.965, "9.3 pb^{-1} (13.6 TeV)");
    //latex.DrawLatex(0.68, 0.965, "1 pb^{-1} (13.6 TeV)");
    //latex.DrawLatex(0.65, 0.965, "30 pb^{-1} (13.6 TeV)");
}


void drawResidual( TFile* f1, TCanvas* c1, string savePath, float xrange=3, Color_t color=2 ){
    CMSstyle();
    gStyle->SetOptFit(101);
    gStyle->SetFitFormat("3.3g");
    //gStyle->SetStatX(0.4);      // Set x-position (fraction of pad size)
    //gStyle->SetStatY(0.9);      // Set y-position (fraction of pad size)
    //gStyle->SetStatW(0.18);      // Set width of stat-box (fraction of pad size)
    //gStyle->SetStatH(0.2);      // Set height of stat-box (fraction of pad size)

    TH1D* pF = (TH1D*)f1->Get("ESAlignmentTool/ESpF_residualX");  
    TH1D* pR = (TH1D*)f1->Get("ESAlignmentTool/ESpR_residualY");  
    TH1D* mF = (TH1D*)f1->Get("ESAlignmentTool/ESmF_residualX");  
    TH1D* mR = (TH1D*)f1->Get("ESAlignmentTool/ESmR_residualY");  

    cout<<"=============== +Front, X-Residual ================="<<endl;	fitResidual(pF,"+Front, X-Residual(cm)",color);	cout<<endl;
    cout<<"=============== +Rear, X-Residual  ================="<<endl;	fitResidual(pR,"+Rear, Y-Residual(cm)",color);	cout<<endl;
    cout<<"=============== -Front, X-Residual ================="<<endl;	fitResidual(mF,"-Front, X-Residual(cm)",color);	cout<<endl;
    cout<<"=============== -Rear, X-Residual  ================="<<endl;	fitResidual(mR,"-Rear, Y-Residual(cm)",color);	cout<<endl;
    pF->UseCurrentStyle(); pF->GetXaxis()->SetRangeUser(-1*xrange,xrange); pF->GetYaxis()->SetRangeUser(0,pF->GetMaximum()+(pF->GetMaximum())/2);
    pR->UseCurrentStyle(); pR->GetXaxis()->SetRangeUser(-1*xrange,xrange); pR->GetYaxis()->SetRangeUser(0,pR->GetMaximum()+(pR->GetMaximum())/2);
    mF->UseCurrentStyle(); mF->GetXaxis()->SetRangeUser(-1*xrange,xrange); mF->GetYaxis()->SetRangeUser(0,mF->GetMaximum()+(mF->GetMaximum())/2);
    mR->UseCurrentStyle(); mR->GetXaxis()->SetRangeUser(-1*xrange,xrange); mR->GetYaxis()->SetRangeUser(0,mR->GetMaximum()+(mR->GetMaximum())/2);
    
    setStyle(pF); setStyle(pR); setStyle(mF); setStyle(mR);

    TLine* line0_pF = new TLine(0.,0.,0.,pF->GetMaximum()); line0_pF->SetLineStyle(7);
    TLine* line0_pR = new TLine(0.,0.,0.,pR->GetMaximum()); line0_pR->SetLineStyle(7);
    TLine* line0_mF = new TLine(0.,0.,0.,mF->GetMaximum()); line0_mF->SetLineStyle(7);
    TLine* line0_mR = new TLine(0.,0.,0.,mR->GetMaximum()); line0_mR->SetLineStyle(7);

    TGaxis::SetMaxDigits(3);

    c1->Clear();
    c1->Divide(2,2);
    c1->cd(1);
    pF->Draw("pe");
    line0_pF->Draw();
    c1->cd(2);
    pR->Draw("pe");
    line0_pR->Draw();
    c1->cd(3);
    mF->Draw("pe");
    line0_mF->Draw();
    c1->cd(4);
    mR->Draw("pe");
    line0_mR->Draw();

    c1->SaveAs( (savePath+".png").c_str());
    c1->SaveAs( (savePath+".pdf").c_str());

}

void drawResidual_BeforeAfter( TFile* f1, TFile* f2, TCanvas* c1, string savePath, float xrange=3, Color_t color=2 ){
    CMSstyle();
    gStyle->SetOptFit(101);
    gStyle->SetFitFormat("3.3g");

    // before
    TH1D* pF1 = (TH1D*)f1->Get("ESAlignmentTool/ESpF_residualX");  
    TH1D* pR1 = (TH1D*)f1->Get("ESAlignmentTool/ESpR_residualY");  
    TH1D* mF1 = (TH1D*)f1->Get("ESAlignmentTool/ESmF_residualX");  
    TH1D* mR1 = (TH1D*)f1->Get("ESAlignmentTool/ESmR_residualY");  

    pF1->UseCurrentStyle(); pF1->GetXaxis()->SetRangeUser(-1*xrange,xrange); pF1->GetYaxis()->SetRangeUser(0,pF1->GetMaximum()+(pF1->GetMaximum())/2);
    pR1->UseCurrentStyle(); pR1->GetXaxis()->SetRangeUser(-1*xrange,xrange); pR1->GetYaxis()->SetRangeUser(0,pR1->GetMaximum()+(pR1->GetMaximum())/2);
    mF1->UseCurrentStyle(); mF1->GetXaxis()->SetRangeUser(-1*xrange,xrange); mF1->GetYaxis()->SetRangeUser(0,mF1->GetMaximum()+(mF1->GetMaximum())/2);
    mR1->UseCurrentStyle(); mR1->GetXaxis()->SetRangeUser(-1*xrange,xrange); mR1->GetYaxis()->SetRangeUser(0,mR1->GetMaximum()+(mR1->GetMaximum())/2);

    pF1->GetXaxis()->SetTitle("+Front, X-Residual (cm)");
    pR1->GetXaxis()->SetTitle("+Rear, Y-Residual (cm)");
    mF1->GetXaxis()->SetTitle("#minusFront, X-Residual (cm)");
    mR1->GetXaxis()->SetTitle("#minusRear, Y-Residual (cm)");
    
    setStyle(pF1, kBlack, 25); setStyle(pR1, kBlack, 25); setStyle(mF1, kBlack, 25); setStyle(mR1, kBlack, 25);

    // after
    TH1D* pF2 = (TH1D*)f2->Get("ESAlignmentTool/ESpF_residualX");  
    TH1D* pR2 = (TH1D*)f2->Get("ESAlignmentTool/ESpR_residualY");  
    TH1D* mF2 = (TH1D*)f2->Get("ESAlignmentTool/ESmF_residualX");  
    TH1D* mR2 = (TH1D*)f2->Get("ESAlignmentTool/ESmR_residualY");  

    pF2->UseCurrentStyle(); pF2->GetXaxis()->SetRangeUser(-1*xrange,xrange); pF2->GetYaxis()->SetRangeUser(0,pF2->GetMaximum()+(pF2->GetMaximum())/2);
    pR2->UseCurrentStyle(); pR2->GetXaxis()->SetRangeUser(-1*xrange,xrange); pR2->GetYaxis()->SetRangeUser(0,pR2->GetMaximum()+(pR2->GetMaximum())/2);
    mF2->UseCurrentStyle(); mF2->GetXaxis()->SetRangeUser(-1*xrange,xrange); mF2->GetYaxis()->SetRangeUser(0,mF2->GetMaximum()+(mF2->GetMaximum())/2);
    mR2->UseCurrentStyle(); mR2->GetXaxis()->SetRangeUser(-1*xrange,xrange); mR2->GetYaxis()->SetRangeUser(0,mR2->GetMaximum()+(mR2->GetMaximum())/2);
    
    setStyle(pF2, kRed, 20); setStyle(pR2, kRed, 20); setStyle(mF2, kRed, 20); setStyle(mR2, kRed, 20);

    // plot
    TLine* line0_pF = new TLine(0.,0.,0.,pF1->GetMaximum()); line0_pF->SetLineStyle(7);
    TLine* line0_pR = new TLine(0.,0.,0.,pR1->GetMaximum()); line0_pR->SetLineStyle(7);
    TLine* line0_mF = new TLine(0.,0.,0.,mF1->GetMaximum()); line0_mF->SetLineStyle(7);
    TLine* line0_mR = new TLine(0.,0.,0.,mR1->GetMaximum()); line0_mR->SetLineStyle(7);

    TLegend* legend = new TLegend(0.60, 0.75, 0.87, 0.90);
    legend->SetLineColor(0);
    legend->SetTextSize(0.04);
    legend->AddEntry(pF1, "Before Alignment", "p");
    legend->AddEntry(pF2, "After Alignment", "p");

    TGaxis::SetMaxDigits(3);
    TGaxis::SetExponentOffset(-0.08, 0.00, "y");


    c1->Clear();
    c1->Divide(2,2);
    c1->cd(1);
    pF1->Draw("pe");
    pF2->Draw("pe,same");
    legend->Draw("same");
    annotate();
    line0_pF->Draw();

    c1->cd(2);
    pR1->Draw("pe");
    pR2->Draw("pe,same");
    legend->Draw("same");
    annotate();
    line0_pR->Draw();

    c1->cd(3);
    mF1->Draw("pe");
    mF2->Draw("pe,same");
    legend->Draw("same");
    annotate();
    line0_mF->Draw();

    c1->cd(4);
    mR1->Draw("pe");
    mR2->Draw("pe,same");
    legend->Draw("same");
    annotate();
    line0_mR->Draw();

    c1->SaveAs( (savePath+".png").c_str());
    c1->SaveAs( (savePath+".pdf").c_str());

}

void draw4CorResidual( TFile* f1, string outputName, int plan, Color_t color=2 ){ //plain 1:pF, 2:pR, 3:mF, 4:mR
    string planName;
    string DirctionOfResi;
    switch (plan){
        case 1:
            planName = "ESpF_resiX";
            DirctionOfResi = "X-Residual";
            break;
        case 2:
            planName = "ESpR_resiY";
            DirctionOfResi = "Y-Residual";
            break;
        case 3:
            planName = "ESmF_resiX";
            DirctionOfResi = "X-Residual";
            break;
        case 4:
            planName = "ESmR_resiY";
            DirctionOfResi = "Y-Residual";
            break;
        default:
            cout<<"You should give 3 iterm a the right number as following";
            cout<<"1:pF, 2:pR, 3:mF, 4:mR"<<endl;
            return;
    }

    cout<<"#############################################################################################"<<endl;
    cout<<"######################### 4Corner Residual:"<<outputName<<", "<<planName<<" #########################"<<endl;
    cout<<"#############################################################################################"<<endl;
    CMSstyle();
    string top 	= "h_"+planName+"_Top";		string xNameT = "Top, "+DirctionOfResi+"(cm)";
    string bottom	= "h_"+planName+"_Bottom";	string xNameB = "Bottom, "+DirctionOfResi+"(cm)";
    string left	= "h_"+planName+"_Left";	string xNameL = "Left, "+DirctionOfResi+"(cm)";
    string right	= "h_"+planName+"_Right";	string xNameR = "Right, "+DirctionOfResi+"(cm)";
    TH1D* TOP 	= (TH1D*)f1->Get(top.c_str()); 
    TH1D* BOTTOM 	= (TH1D*)f1->Get(bottom.c_str()); 
    TH1D* LEFT 	= (TH1D*)f1->Get(left.c_str()); 
    TH1D* RIGHT 	= (TH1D*)f1->Get(right.c_str()); 
    string savePath = "png/Residual_4Corner_"+outputName+"_"+planName+".png";

    cout<<"=============== Top, "<<DirctionOfResi<<" ================="<<endl;	fitResidual(TOP, xNameT, color);	cout<<endl;
    cout<<"=============== Bottom, "<<DirctionOfResi<<" ================="<<endl;	fitResidual(BOTTOM, xNameB, color);	cout<<endl;
    cout<<"=============== Left, "<<DirctionOfResi<<" ================="<<endl;	fitResidual(LEFT, xNameL, color);	cout<<endl;
    cout<<"=============== Right, "<<DirctionOfResi<<" ================="<<endl;	fitResidual(RIGHT, xNameR, color);	cout<<endl;
    TOP->UseCurrentStyle();		TOP->GetXaxis()->SetRangeUser(-3,3);
    BOTTOM->UseCurrentStyle();	BOTTOM->GetXaxis()->SetRangeUser(-3,3);
    LEFT->UseCurrentStyle();	LEFT->GetXaxis()->SetRangeUser(-3,3);
    RIGHT->UseCurrentStyle();	RIGHT->GetXaxis()->SetRangeUser(-3,3);

    TCanvas* c1 = new TCanvas("c1", "", 850,700);
    c1->Divide(2,2);
    c1->cd(1);
    TOP->Draw("pe");
    c1->cd(2);
    BOTTOM->Draw("pe");
    c1->cd(3);
    LEFT->Draw("pe");
    c1->cd(4);
    RIGHT->Draw("pe");
    c1->SaveAs(savePath.c_str());


}

