% Short report setup, David Orn Johannesson ; davidj11@ru.is


\newcommand{\fileversion@rureport}{v0.1}
\newcommand{\filedate@rureport}{2014-mai-30}
\newcommand{\fileauthor@rureport}{David Orn Johannesson, davidj11@RU.IS}
\NeedsTeXFormat{LaTeX2e}


%% ---------------- Initial Code -----------------------------
\RequirePackage{ifthen}
% This package allows you to create conditionals on booleans
\RequirePackage{ifdraft}
\newboolean{svninfo}
\DeclareOption{svninfo}{
  \setboolean{svninfo}{true}
}
%% now we pass the remaining unused options to our parent class
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
%% ---------------- Execution of Options -----------------------------
\ProcessOptions \relax % this stops searching for a * in
                       % \ProcessOtions*
%% ---------------- Package Loading -----------------------------
\LoadClass{article}  % our parent class.  Article is a little easier
                     % to work with than the report class.


%% -------------Language setup, set to icelandic -------------------
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}  % allows UTF encoding, needed for Icelandic characters
\RequirePackage[icelandic]{babel} 	% ignoring this package makes 
									% English the main language
									
									
%% -----------------Graphics setup --------------------------------

\RequirePackage{float}
\RequirePackage[final]{graphicx}
\RequirePackage{epstopdf}

%% Import a graphics folder for graphcis and set the types allowed
\DeclareGraphicsExtensions{.pdf,.jpeg,.jpg,.png,.gif,.PDF,.JPEG,.JPG,.PNG,.GIF}
%% The extensions that it will search for as valid graphics files
\graphicspath{{/graphics/}{Graphics/}}
\RequirePackage[final]{pdfpages}
%% The "pdfpages" package lets you include PDF documents into your
%% document but keeps the formatting consistent (headers, footers,
%% etc.)

%% URL setup
\RequirePackage{url}


%% ------------------ Text setup -----------------------------------
\RequirePackage[left = 2.0cm, right=2.0 cm, top=4.0 cm, bottom=3.0 cm]{geometry}

% Remove indentation
\setlength\parindent{0pt}
\linespread{1.3}
% this is for the picture environment
\setlength{\unitlength}{1cm}
		%% Choose the font package
%\RequirePackage{lmodern}
\RequirePackage{times}
%\RequirePackage{palatino}
%\RequirePackage{bookman}
%\RequirePackage{newcent}
%\RequirePackage{helvet}
\renewcommand{\familydefault}{\sfdefault}

% Maths
\RequirePackage{amsfonts}
\RequirePackage[amssymb]{SIunits}
\RequirePackage{SIunits} % allows you to use units in a more
                         % standardized way e.g. 100~\mega\newton\per\square\meter{}

% Chemsetry
\RequirePackage[version = 3]{mhchem}

\RequirePackage{subfig}
%% Nice package for making sub figures inside of a figure.  Keeps all
%% the reference labels correct and makes "sub captions"
%% 
%% 
%% **********Special symbols for file**************************

%% Commonly used notation/abbrevs, converted into latex commands:
\renewcommand{\d}[1]{\;\textsf{d}#1}
\newcommand{\pd}[1]{\partial #1}
\newcommand{\D}{\;\textsf{D}}
\providecommand{\e}[1]{\ensuremath{\times 10^{#1}}}
%% Extremely common abbreviations
\newcommand{\kg}{\kilo\gram\xspace}
\newcommand{\mA}{\milli\ampere\xspace}
\newcommand{\amp}{\ampere\xspace}

%% ********************Frontpage setup**************************

%% ----- Setup page layout, including title page ----- %%

%% First we need to create some "variables" with defaults and commands
%% defaults
\newcommand{\title@rureport}{Unlabelled}
\newcommand{\author@rureport}{Davíð Örn Jóhannesson}
\newcommand{\course@rureport}{Sonus Ceti}
\newcommand{\version@rureport}{V. 0.0}

%% commands to set them
\renewcommand{\title}[1]{\renewcommand{\title@rureport}{#1}}
\renewcommand{\author}[1]{\renewcommand{\author@rureport}{#1}}
\newcommand{\course}[1]{\renewcommand{\course@rureport}{#1}}
\newcommand{\instructor}[1]{\renewcommand{\instructor@rureport}{#1}}

%% Version numver set
\newcommand{\version}[1]{\renewcommand{\version@rureport}{V. #1}}

\newcommand{\shorttitle}{\ifdraft{DRAFT:}{} \title@rureport}

\renewcommand{\maketitle}{
  {\centering%

    {\LARGE
      \ifdraft{\fbox{DRAFT!  DO NOT SUBMIT!}\\}{}
      
      
      \vspace{\baselineskip}  
      \vspace{15 mm}  
      \vspace{\baselineskip}  
      
      {\huge \title@rureport\\}
      
      \vspace{\baselineskip}  
      \vspace{\baselineskip}  
	\includegraphics{ru-logo}\\\vspace{\baselineskip}
      \vspace{\baselineskip} 
      \vspace{\baselineskip}            
      
      \large
      \course@rureport\\
      \author@rureport\\

    }
    {\large
      \vfill
      \today\\    
      
	\thispagestyle{empty} 
    }

  }
  \newpage

  \setcounter{page}{1}  
}





\RequirePackage[nottoc,notlot,notlof]{tocbibind}


%% ---------------- End of Class --------------------------

\AtBeginDocument{
  \RequirePackage[final]{hyperref}  
%% Hyper references (clickable links) in the document.  Very nice, but
%% MUST be the last package loaded.  If you are in draft mode, it will
%% disable itself, so we force it to be in final mode.
  \RequirePackage{fancyhdr}
  \fancyhf{}
  \lhead{Sonus Ceti}
}