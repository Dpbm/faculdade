import { Component, Input, OnInit } from '@angular/core';
import { Likes } from '../likes/likes.component';

@Component({
  standalone: true,
  selector: 'card',
  imports: [Likes],
  styleUrl: './card.component.css',
  templateUrl: './card.component.html',
})
export class Card implements OnInit {
  @Input() title: string = '';
  @Input() subtitle: string = '';

  image: string = '';
  imageAlt: string = '';

  ngOnInit() {
    this.image =
      'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExczV3Mmh2ZGR1amRmNDYyOWVlZjc2ZDJ4NTB6ZmpweXpoYTd5bTk1biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fBG7UnBi7QtePFHEnk/giphy.gif';
    this.imageAlt = 'teu cu';
  }
}
