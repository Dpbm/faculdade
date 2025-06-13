import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'likes',
  imports: [CommonModule],
  styleUrl: './likes.component.css',
  templateUrl: './likes.component.html',
})
export class Likes {
  likes: number = 0;
  overpower: boolean = false;

  addLike() {
    if (this.likes > 10) {
      this.overpower = true;
    } else {
      this.likes++;
    }
  }
}
