﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PZ_APP.Models
{
    public class BaseEquationModel
    {
        public double BaseScore { get; set; }
        public double Impact { get; set; }
        public double Exploitability { get; set; }
        public double fImpact { get; set; }
        public double AccessVectorNumber { get; set; }
        public double AccessComplexityNumber { get; set; }
        public double AuthenticationNumber { get; set; }
        public double ConfImpactNumber { get; set; }
        public double IntegImpactNumber { get; set; }
        public double AvailImpactNumber { get; set; }

        public string AccessVectorString { get; set; }
        public string AccessComplexityString{ get; set; }
        public string AuthenticationString { get; set; }
        public string ConfImpactString { get; set; }
        public string IntegImpactString { get; set; }
        public string AvailImpactString { get; set; }



    }
}
