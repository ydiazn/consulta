jQuery.fn.BirthdateFromCI = function(opts){
	// Merge passed options with defaults
    var opts = opts || {};
    var date

    function calculateYear(ci, year){
    	_year = ci.substring(0, 2);   
        year = getLast2DigitYear(year);

        if(parseInt(_year) > year)
            //siglo 20
            year = "19";
        else
            //siglo 21
            year = "20";

        return year.concat(_year);    
    }

    function getLast2DigitYear(year){
        year = new Number(year).toString();
    	return parseInt(year.substring(2, 4));    
    }

    $(this).change(function(){
        date = new Date();
        year = date.getFullYear();
     
        ci = $(this).val();
        year = calculateYear(ci, year);
        month = ci.substring(2, 4);
        day = ci.substring(4, 6);

        opts.birthdate.val(day + "/" + month + "/" + year);
    });
};

console.log('yes');
