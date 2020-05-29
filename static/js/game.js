
$(document).ready(function(){

    var app= {
cards:[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8],
// do function in these cards. suffle cards 
//and assign number to each of the card

init: function() {
    app.shuffle();
    app.assignCards();
},


shuffle: function() {
    var random = 0;
    var temp = 0;
    for(i = 1; i < app.cards.length; i++){
random = Math.round (Math.random() * i);
temp = app.cards [i];
app.cards[i] = app.cards[random];
app.cards[random] = temp;
}

app.assignCards();
console.log('Shaffled Card Array:'+app.cards);
},


assignCards: function() {
$('.card').each(function(index) {
    $(this).attr('data-card-value', app.cards[index]);
});


app.clickHandlers();
},
//when cards is clicked display
// the asiigned number of the card on this card

clickHandlers: function() {
    $('.card').on('click', function() {
        $(this).html('<p>'+$(this).data('cardValue')+'</p>').addClass('selected');
        app.checkMatch();

    });
},


//if two are selected and they match
checkMatch: function() {
if($('.selected').length === 2) {
    if($('.selected').first().data('cardValue') === $('.selected').last().data('cardValue')){
        $('.selected').each(function() {
          $(this).animate({opacity: 0}).removeClass('unmatched');
        });

       $('.selected').each(function() {
           $(this).removeClass('selected');
       });
       app.checkWin();


    } else {
        //for each of the selected cards in this document remove selected

setTimeout(function() {
    $('.selected').each(function() {
    $(this).html('').removeClass('selected');
});
}, 1000);
        }
    }

},



//if there is no exist cards left(length===0) in container of cards
// of this html file => you won.


checkWin: function() {
if($('.unmatched').length === 0) {
$('.container').html('');

}

    }

};
app.init();

});


